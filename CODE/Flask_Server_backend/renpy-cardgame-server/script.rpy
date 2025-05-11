define player_name = "Player1"  # Change to Player2, Player3 on other machines if needed

label start:
    scene bg room

    "Welcome to the Multiplayer Card Game!"
    jump card_game

label card_game:
    python:
        cards = ["Ace of Spades", "2 of Hearts", "Queen of Diamonds", "King of Clubs"]
        selected_card = None

    "Choose a card to play:"

    menu:
        for card in cards:
            $ card_label = card
            "{card_label}":
                $ selected_card = card
                jump send_card

label send_card:
    "Sending your move to the server..."
    $ result = send_move_to_server(player_name, selected_card)

    if "error" in result:
        "Something went wrong: [result['error']]"
    else:
        "Move sent! Server says: [result['status']]"

    jump fetch_game_state

label fetch_game_state:
    "Fetching the current game state..."
    $ state = get_game_state()

    if "error" in state:
        "Failed to fetch game state: [state['error']]"
    else:
        "Here are the latest moves from all players:"
        python:
            moves = state.get("moves", [])

        if moves:
            for move in moves:
                "[move['player']] played [move['card']]"
        else:
            "No moves yet."

    menu:
        "What would you like to do next?":
            "Play another card":
                jump card_game
            "Quit game":
                return
