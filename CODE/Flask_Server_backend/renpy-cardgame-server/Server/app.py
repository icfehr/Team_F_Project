from flask import Flask, request, jsonify, render_template_string
from flask_socketio import SocketIO, emit
import sqlite3
import requests

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# Game state
players = {}
move_history = []
current_turn = None

# Initialize DB
def init_db():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_moves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            player_name TEXT,
            move_details TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

# Function to send the current game state to another server
def table_push(ip, player_id, player_name, player_hand, current_turn, player_score):
    try:
        game_state = {
            "player_id": player_id,
            "player_name": player_name,
            "cards_in_hand": [card.to_dict() if hasattr(card, "to_dict") else card for card in player_hand],
            "current_turn": current_turn,
            "score": player_score
        }

        response = requests.post(f"http://{ip}/register", json=game_state)
        if response.status_code == 200:
            print("Game state successfully sent to the server.")
            return True
        else:
            print(f"Failed to send game state: {response.status_code}")
            return False
    except Exception as e:
        print(f"Error while sending game state: {e}")
        return False

@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"}), 200

@app.route('/register', methods=['POST'])
def register_player():
    data = request.get_json()
    player_name = data.get('player_name')

    if not player_name:
        return jsonify({"error": "Missing 'player_name'"}), 400

    players[player_name] = {
        "hand": data.get('cards_in_hand', []),
        "score": data.get('score', 0)
    }

    print(f"[REGISTER] {player_name} registered with hand: {players[player_name]['hand']}")
    return jsonify({"message": f"Player {player_name} registered successfully"}), 200

@app.route('/join', methods=['POST'])
def join_game():
    global current_turn
    data = request.get_json()
    player_name = data.get('player')
    if not player_name:
        return jsonify({"error": "Missing 'player' field"}), 400

    if player_name not in players:
        players[player_name] = {'score': 0, 'hand': []}
        if current_turn is None:
            current_turn = player_name

    return jsonify({"message": f"Player {player_name} joined!"}), 200

def save_move(player_name, move_details):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game_moves (player_name, move_details) VALUES (?, ?)", (player_name, move_details))
    conn.commit()
    conn.close()

@app.route('/move', methods=['POST'])
def make_move():
    global current_turn
    data = request.get_json()
    player_name = data.get('player')
    move_details = data.get('move_details')

    if not player_name or not move_details:
        return jsonify({"error": "Missing 'player' or 'move_details'"}), 400

    if player_name != current_turn:
        return jsonify({"error": "It's not your turn!"}), 403

    save_move(player_name, move_details)
    move_history.append((player_name, move_details))
    players[player_name]['score'] += 1

    # Switch turns
    all_players = list(players.keys())
    if len(all_players) > 1:
        current_index = all_players.index(player_name)
        next_index = (current_index + 1) % len(all_players)
        current_turn = all_players[next_index]

    # Update game state to server
    server_ip = "127.0.0.1"
    player_id = 1  # Dummy ID
    player_hand = players[player_name]['hand']
    player_score = players[player_name]['score']
    table_push(server_ip, player_id, player_name, player_hand, current_turn, player_score)

    socketio.emit('move_made', {'player': player_name, 'move': move_details})
    return jsonify({"status": "move saved", "next_turn": current_turn}), 200

@app.route('/play', methods=['POST'])
def play_game():
    data = request.get_json()
    player_name = data.get('player')

    if player_name not in players:
        return jsonify({"error": f"Player {player_name} not found."}), 400

    players[player_name]['score'] += 1
    return jsonify({
        "message": f"{player_name} made a move.",
        "player_score": players[player_name]['score']
    }), 200

# ✅ NEW: Game State Route
@app.route('/state', methods=['GET'])
def get_game_state():
    return jsonify({
        "players": players,
        "current_turn": current_turn,
        "move_history": move_history
    }), 200

@app.route('/admin', methods=['GET'])
def admin_panel_json():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game_moves ORDER BY timestamp DESC")
    moves = cursor.fetchall()
    conn.close()

    move_list = [
        {"id": row[0], "player_name": row[1], "move_details": row[2], "timestamp": row[3]}
        for row in moves
    ]

    return jsonify({
        "players": players,
        "current_turn": current_turn,
        "moves": move_list
    }), 200

@app.route('/admin-panel', methods=['GET'])
def admin_panel_html():
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM game_moves ORDER BY timestamp DESC")
    moves = cursor.fetchall()
    conn.close()

    move_list = [
        {"id": row[0], "player_name": row[1], "move_details": row[2], "timestamp": row[3]}
        for row in moves
    ]

    html_template = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Game Admin Panel</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #1e1e2f;
                color: #ffffff;
                padding: 20px;
            }
            h1 {
                color: #00d1b2;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
                background-color: #2c2c3c;
            }
            th, td {
                padding: 12px;
                border: 1px solid #444;
                text-align: left;
            }
            th {
                background-color: #3d3d5c;
            }
            tr:nth-child(even) {
                background-color: #33334d;
            }
        </style>
    </head>
    <body>
        <h1>Admin Panel: Game Moves</h1>
        <p><strong>Current Turn:</strong> {{ current_turn or "None" }}</p>
        <table>
            <tr>
                <th>ID</th>
                <th>Player</th>
                <th>Move</th>
                <th>Timestamp</th>
            </tr>
            {% for move in moves %}
            <tr>
                <td>{{ move.id }}</td>
                <td>{{ move.player_name }}</td>
                <td>{{ move.move_details }}</td>
                <td>{{ move.timestamp }}</td>
            </tr>
            {% endfor %}
        </table>
    </body>
    </html>
    '''

    return render_template_string(html_template, moves=move_list, current_turn=current_turn)

@socketio.on('make_move')
def handle_socket_move(data):
    player_name = data.get('player')
    move_details = data.get('move')

    if player_name and move_details:
        save_move(player_name, move_details)
        emit('move_made', data, broadcast=True)

# Run the app
if __name__ == '__main__':
    init_db()
    socketio.run(app, debug=True)
