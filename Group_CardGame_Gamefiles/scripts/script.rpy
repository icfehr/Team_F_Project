# script.rpy

init python:
    import socketio
    import requests

    # Connect to the server
    sio = socketio.Client()

    # Connect to the Flask server
    sio.connect("http://127.0.0.1:5000")

    # Function to send a move
    def send_move(player_name, move_details):
        sio.emit("make_move", {"player": player_name, "move": move_details})

    # Listen for move updates from the server
    @sio.event
    def move_made(data):
        player = data['player']
        move = data['move']
        renpy.say(player, f"Moved: {move}")

label start:
    scene bg arena
    "For the purposes of this demo, the game loads directly into the given duel arena."

    # Multiplayer connection block
    $ ip = "127.0.0.1"
    $ success = False

    python:
        try:
            response = requests.get(f'http://{ip}:5000/ping')
            if response.status_code == 200:
                success = True
        except requests.exceptions.RequestException:
            success = False

    if not success:
        "Could not reach the server!"
        return

    $ player_name = "Angel"
    $ response = requests.post(f'http://{ip}:5000/join', json={"player": player_name})

    if response.status_code == 200:
        $ player_data = response.json()
        "You are connected!"
        # Show player's hand
        "Your hand: [player_data['hand']]"
    else:
        "Failed to register."

    # Example of sending a move
    $ move = "Played Card X"
    python:
        send_move("Angel", move)

    return
