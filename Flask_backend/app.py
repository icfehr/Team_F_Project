from flask import Flask, render_template, request, jsonify
import sqlite3
import random
import os

app = Flask(__name__)
DATABASE = 'game.db'

deck = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
players = {}

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS moves (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                player TEXT,
                card TEXT,
                result TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute("SELECT player, card, result, timestamp FROM moves ORDER BY timestamp DESC")
        rows = c.fetchall()
    return render_template('admin.html', moves=rows)

@app.route('/join', methods=['POST'])
def join():
    name = request.json.get("player")
    if name not in players:
        hand = random.sample(deck, 5)
        players[name] = {"hand": hand, "score": 0}
    return jsonify({"hand": players[name]["hand"]})

@app.route('/play', methods=['POST'])
def play():
    data = request.json
    player = data['player']
    if player in players and players[player]['hand']:
        played = players[player]['hand'].pop(0)
        win = played == 'Ace'
        result = "Win" if win else "Continue"
        if win:
            players[player]['score'] += 1
        with sqlite3.connect(DATABASE) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO moves (player, card, result) VALUES (?, ?, ?)",
                      (player, played, result))
            conn.commit()
        return jsonify({
            "playedCard": played,
            "newHand": players[player]['hand'],
            "result": result,
            "score": players[player]['score']
        })
    return jsonify({"message": "No cards left"}), 400

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
