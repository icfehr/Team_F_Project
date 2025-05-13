label start:
    "Welcome to the Multiplayer Card Game!"

    menu:
        "Start New Game":
            $ renpy.python.pure_eval('''
import requests
requests.post("http://127.0.0.1:5000/start_game", json={"player1_id": 1, "player2_id": 2})
''')
            "Game started between Player 1 and Player 2."

        "Draw card for Player 1":
            $ card = renpy.python.pure_eval('''
import requests
res = requests.post("http://127.0.0.1:5000/draw_card", json={"game_id": 1, "player_id": 1})
res.json()["card"]
''')
            "Player 1 drew a [card]."

        "Draw card for Player 2":
            $ card = renpy.python.pure_eval('''
import requests
res = requests.post("http://127.0.0.1:5000/draw_card", json={"game_id": 1, "player_id": 2})
res.json()["card"]
''')
            "Player 2 drew a [card]."

    return
