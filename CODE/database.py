import sqlite3

def init_db():
    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS players
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)''')
    conn.commit()
    conn.close()

def add_player(player_name):
    conn = sqlite3.connect('game.db')
    c = conn.cursor()
    c.execute("INSERT INTO players (name) VALUES (?)", (player_name,))
    conn.commit()
    player_id = c.lastrowid
    conn.close()
    return player_id
