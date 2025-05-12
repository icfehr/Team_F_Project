# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
define a = Character('Angel', color="#8f8f8f")

# Game starts here
label start:

    # Show a background image for the arena (You can replace with your actual image later)
    scene bg arena

    # Show a test image or sprite for now (you can replace this with actual character sprites later)
    show eileen happy

    ### DEBUG ###
    # Insert test image screen here (this can be a debug screen showing something specific for testing purposes)
    $ renpy.call_in_new_context("start_duel", enemy_deck)
    ### DEBUG ###

    # Display a greeting message
    "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"

    # Starting a duel: You will integrate the game flow and logic here.
    $ player_id = "player1"
    $ player_name = "Angel"
    $ game_id = "game1"

    # Join the game via Flask backend
    $ join_game_to_flask(player_id, player_name, game_id)

    # Let's simulate a card move
    $ send_move_to_server(game_id, player_id, "card1")

    # Broadcast game update to all players
    $ broadcast_game_update(game_id, player_id)

    "Game started and move sent!"

    # After joining the game, continue the flow to start the duel
    $ renpy.pause(1)  # Pause to let the game logic process for a moment

    # Start duel
    jump duel

# The duel starts here. This label will handle the logic for the duel and related actions.
label duel:
    # This label starts the duel, and can include gameplay logic.
    "The duel begins!"

    # Example of showing the enemy deck or the opponent's cards (can be dynamic later)
    show enemy_deck

    # Here, you can add the duel gameplay logic, such as turns, player moves, etc.
    # For now, we'll just display some placeholder text.

    "It's your turn to make a move. Choose a card to play."

    return
