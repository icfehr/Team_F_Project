from flask import Blueprint, request, jsonify
from .database import save_move, get_game_state

routes = Blueprint('routes', __name__)

@routes.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "ok"}), 200

@routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    # Add logic to register player
    return jsonify({"message": "Player registered."}), 200

@routes.route("/move", methods=["POST"])
def move():
    data = request.get_json()
    save_move(data)
    return jsonify({"message": "Move saved."}), 200

@routes.route("/game-state", methods=["GET"])
def game_state():
    state = get_game_state()
    return jsonify(state), 200
