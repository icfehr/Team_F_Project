# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:

    "For the Purposes of this Demo the game loads directly into the given duel arena"

    "Later on this will instead be a menu where you can select the game mode, single player, multiplayer, and deck building with unlocked cards."

    "This is a demo of the game and not the final version."
    "The game is currently in development and not all features are implemented yet."
    "There are many game assets that are not final or missing, and will be updated in the future."

    ###DEGBUG###
    ### INSTERT TEST IMAGE SCREEN HERE ###
    show bg arena
    with dissolve
    #jump to basic_functionality label 
    jump basic_functionality
    show screen black

    "As you can see the game functionality and logic is working."

    "Next steps would be to verify multiplayer functionality over the network instead of just connecting to the server."

    # This ends the game.

    return


screen basic_functionality_menu:
    modal True
    hbox:
        spacing 50
        yalign 0.5
        imagebutton:
            idle "images/cards/border.webp"
            focus_mask True
            action [Notify("Button Disabled, Deck Builder not implemented")]
        imagebutton:
            idle "images/cards/border.webp"
            focus_mask True
            action [Hide('basic_functionality_menu'), Jump('jump_point')]
        imagebutton:
            idle "images/cards/border.webp"
            focus_mask True
            action [Notify("Button Disabled, Card Shop not implemented")]

label jump_point:
    $ renpy.call_in_new_context("start_duel", enemy_deck)
    jump ending
    return

label basic_functionality:
    "This screen was originally designed to be a menu screen."
    "As it is now only the center button is functional."
    "The center button will start a new game of the card game."
    "If the server is active it will send out a push request to the server, later on this would have triggered a function in the server to start a multiplayer instance."
    "The game would have then used a basic matchmaking system based on player ID and Win loss ratio to make the match."
    "On the right would have been a card shop where you could buy cards and unlock new ones."
    "On the left would have been a deck builder where you could build your deck and select the cards you want to use."
    "As our group only had 3 people for development obviously many planned functionalities had to be cut from the final demo."
    "However the core gameplay and functionality of the game logic being correct locally and the server receiving game information (should be) working correctly."
    ### Call screen to start menu selection options ###
    show screen basic_functionality_menu
    with dissolve

    label ending:
        "As you can see the game functionality and logic is working."
        "Next steps would be to verify multiplayer functionality over the network instead of just connecting to the server."
        "This would require a second player and a server hosted as a web app instead of a local server we have used for development."
        "However this is not something we were able to implement with the time and people we had available."
        "I hope you enjoyed the demonstration because it was a nightmare to get up and running!"
        "The Game will now return to the main menu."
        "Thank you for playing!"
        return

    ### Should be unable to reach past this point and any code below is a fall back in case of errors. ###
    jump ending


    # jump to ending label .
    "To reach this point something must have gone wrong."
    "The game will now return to the main menu."
    "Please try again later."
    return


