from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Database config (SQLite for now, can be configured for SQL Server later)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'  # Changed to project directory
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Define the database model for Player
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    wins = db.Column(db.Integer, default=0)
    losses = db.Column(db.Integer, default=0)
    games_played = db.Column(db.Integer, default=0)
    score = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'<Player {self.name}>'


# Create the database tables if they do not exist
with app.app_context():
    db.create_all()


# Routes
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Ren'Py Card Game Server is running!"}), 200



###Iain
@app.route("/ping", methods=["GET"])
def ping():
    """Endpoint for client to check server availability."""
    return jsonify({"status": "ok"}), 200

@app.route("/favicon.ico")
def favicon():
    return "", 204  # No content to avoid the 404 error for the favicon


@app.route("/join", methods=["POST"])
def join_game():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Invalid JSON"}), 400

    player_name = data.get('name') # Existing /join expects 'name'

    if not player_name:
        return jsonify({"message": "Missing player name"}), 400

    existing = Player.query.filter_by(name=player_name).first()
    if existing:
        return jsonify({"message": f"Player {player_name} already in the game!"}), 200

    new_player = Player(name=player_name)
    db.session.add(new_player)
    db.session.commit()
    return jsonify({
        "message": f"Player {player_name} joined the game!",
        "player_id": new_player.id,
        "name": new_player.name
    }), 201

@app.route("/register", methods=["POST"])
def register_player():
    """Endpoint for client to register a player, similar to /join."""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Invalid JSON"}), 400

    player_name = data.get('player_name')
    player_id = data.get('player_id')

    if not player_name:
        return jsonify({"message": "Missing player name"}), 400

    player = Player.query.filter_by(name=player_name).first()
    if not player:
        player = Player(name=player_name)
        db.session.add(player)
        db.session.commit()
        return jsonify({"message": f"Player {player_name} registered.", "player_id": player.id}), 201
    return jsonify({"message": f"Player {player_name} already registered.", "player_id": player.id}), 200


@app.route("/update_player", methods=["POST"])
def update_player():
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Invalid JSON"}), 400

    player_name = data.get('name')
    player = Player.query.filter_by(name=player_name).first()

    if not player:
        return jsonify({"message": f"Player {player_name} not found!"}), 404

    # Update player stats (wins, losses, games played, score)
    player.wins = data.get('wins', player.wins)
    player.losses = data.get('losses', player.losses)
    player.score = data.get('score', player.score)  # Update score if provided
    player.games_played += 1
    db.session.commit()
    return jsonify({"message": f"Player {player_name}'s stats updated!"}), 200

###Iain
@app.route("/opponent", methods=["GET"])
def get_opponent_data():
    """Endpoint for client to get opponent data."""
    # This is a placeholder.
    # For now, returning a mock opponent or the first player as an example
    opponent = Player.query.first() # Example: just picking the first player
    if opponent:
        return jsonify({"player_id": opponent.id, "player_name": opponent.name}), 200
    return jsonify({"message": "No opponent data available yet."}), 404




###Iain
@app.route("/move", methods=["POST"])
def record_move():
    # This is a placeholder.

    """Endpoint for client to send a player's move."""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Invalid JSON"}), 400

    player_id = data.get('player_id')
    move_data = data.get('move')

    if player_id is None or move_data is None:
        return jsonify({"message": "Missing player_id or move data"}), 400

    # Placeholder: Logic to save the move to the database
    print(f"Move received from player {player_id}: {move_data}")
    return jsonify({"message": "Move saved."}), 200


@app.route("/game_state", methods=["GET"])
def game_state():
    players = Player.query.all()
    return jsonify({
        "players": [
            {"name": p.name, "wins": p.wins, "losses": p.losses, "games_played": p.games_played, "score": p.score}
            for p in players
        ]
    })


#Iain
#@app.route("/latest_move", methods=["GET"])
#def get_latest_move():
    """Endpoint for client to get the latest move."""
    # Placeholder: Logic to retrieve the latest move from the database
    # e.g., latest_move_obj = Move.query.order_by(Move.timestamp.desc()).first()
    # if latest_move_obj:
    #    return jsonify({"move": latest_move_obj.move_details, "player_id": latest_move_obj.player_id}), 200
#    return jsonify({"move": "No moves recorded yet."}), 200 # Placeholder response

#Iain
@app.route("/board_update", methods=["POST"])
def board_update():
    """Endpoint for client to send the current board state."""
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({"message": "Invalid JSON"}), 400

    player_id = data.get('player_id')
    board_state = data.get('board_state')

    if player_id is None:
        return jsonify({"message": "Missing player_id"}), 400
    if board_state is None:
        return jsonify({"message": "Missing board_state"}), 400

    # Basic validation (optional, can be expanded)
    if not isinstance(board_state, list):
        return jsonify({"message": "board_state should be a list"}), 400

    print(f"Board update received for player_id: {player_id}")
    print(f"Board state: {board_state}") # For debugging, you can pretty-print or process further
    # Placeholder: Here you would add logic to store this board_state in your database,
    # potentially associating it with the player_id and the current game session.
    return jsonify({"message": "Board state received."}), 200




if __name__ == "__main__":
    app.run(debug=True)
