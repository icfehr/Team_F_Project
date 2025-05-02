from flask import Flask, request, jsonify, render_template_string
from flask_socketio import SocketIO, emit
import sqlite3

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

# Ping test
@app.route('/ping', methods=['GET'])
def ping():
    return jsonify({"status": "ok"}), 200

# Join game
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
            current_turn = player_name  # Set the first player to move

    return jsonify({"message": f"Player {player_name} joined!"}), 200

# Save to DB
def save_move(player_name, move_details):
    conn = sqlite3.connect('game.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO game_moves (player_name, move_details) VALUES (?, ?)", (player_name, move_details))
    conn.commit()
    conn.close()

# Move handler
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

    # Switch turn to next player
    all_players = list(players.keys())
    if len(all_players) > 1:
        current_index = all_players.index(player_name)
        next_index = (current_index + 1) % len(all_players)
        current_turn = all_players[next_index]

    socketio.emit('move_made', {'player': player_name, 'move': move_details})

    return jsonify({"status": "move saved", "next_turn": current_turn}), 200

# Score test route
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

# JSON Admin data
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

# HTML Admin dashboard
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

# Socket handler
@socketio.on('make_move')
def handle_socket_move(data):
    player_name = data.get('player')
    move_details = data.get('move')

    if player_name and move_details:
        save_move(player_name, move_details)
        emit('move_made', data, broadcast=True)

# Start server
if __name__ == '__main__':
    init_db()
    socketio.run(app, debug=True)
