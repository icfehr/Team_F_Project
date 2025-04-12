# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.



# The game starts here.

label start:

    scene bg arena
    "For the Purposes of this Demo the game loads directly into the given duel arena"

    "Later on this will instead be a menu where you can select the game mode, single player, multiplayer, and deck building with unlocked cards."

    "This is a demo of the game and not the final version."
    "The game is currently in development and not all features are implemented yet."
    "There are many game assets that are not final or missing, and will be updated in the future."

    ###DEGBUG###
    ### INSTERT TEST IMAGE SCREEN HERE ###
    $ renpy.call_in_new_context("start_duel", enemy_deck)
    ###DEGBUG###

    # These display lines of dialogue.

    "You've created a new Ren'Py game."

    "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
