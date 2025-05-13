init python:
    import random
    import socket  # Make sure socket is imported if get_ip uses it
    import math
    import re
    import functools
    import random


    ### Common Functions 

    def image_hover(image, brightness=0.12):
        """Returns brighter image when hovering over an object"""
        return Transform( image, matrixcolor=BrightnessMatrix(brightness) )

    def image_alpha(image, alpha=0.5):
        """Returns an image with changed alpha 0 - fully transparent 1 - fully visible"""
        return Transform( image, matrixcolor=OpacityMatrix(alpha) )

    def disable_game_menu():
        setattr(renpy.store, "_game_menu_screen", None)

    def enable_game_menu():
        setattr(renpy.store, "_game_menu_screen", "save_screen")
    ### Use to set time limits later 
    def timeit(func, loops=10000, args=(), kwargs={}):
        rv = timeit_module.timeit("func(*args, **kwargs)", number=loops, globals=dict(func=func, args=args, kwargs=kwargs))
        print(f"The task has taken {rv} seconds to finish")


    # Define global variables
    player_name = "Player 1"
    player2_name = "Player 2"
    player_id = 0
    startingimage = "images/start.jpg"
    game_server = "0.0.0.0"  # Placeholder for game server IP address
    opponent_id = 0
    ip = "Unknown"
    # The get_ip function is now expected to be available from webhook.rpy

    def initialize_player_data():
        global player_name, player2_name, player_id, ip, game_server, opponent_id
        player_id = random.randint(1, 10000000000)
        ip = get_ip()  # This will now call the get_ip() from webhook.rpy
        player = playerdata(player_name, player_id)
        player2 = MultiplayerOpponent(player2_name, opponent_id, server=game_server)
        print(f"Player data initialized: ID={player_id}, IP={ip}")

# Initialize variables during a later init phase to ensure webhook.rpy's functions are available
init 5 python:
    initialize_player_data()

image bg arena = "images/cards/card_table.png"
image bg start = "images/cards/start.jpg"
image placeholder = "images/087000_hr1.png"
image bg start = "images/start.jpeg"
image Menu1 = "images/cards/border.webp"
image Menu2 = "images/cards/border.webp"
image Menu3 = "images/cards/border.webp"


image ctc:
    contains:
        pos (0.99, 0.995)
        anchor (0.8, 1.0)
        "cards/ctc00.webp"
    contains:
        pos (0.99, 0.995)
        anchor (0.8, 1.0)
        "cards/ctc01.webp"
        pause 5.0
        linear 1.0 alpha 0.0
        linear 1.0 alpha 1.0
        repeat
