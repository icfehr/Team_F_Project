import sqlite3

def create_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS game_state (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            move_data TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_move(move_data):
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('''
        INSERT INTO game_state (move_data) VALUES (?)
    ''', (move_data,))
    conn.commit()
    conn.close()

def get_all_moves():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('SELECT * FROM game_state')
    moves = c.fetchall()
    conn.close()
    return moves
