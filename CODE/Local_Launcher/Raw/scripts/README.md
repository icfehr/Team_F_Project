### 2025S_CSCI441_VA_Software Engineering
### Team_F_Project
### Card Game
# File put together by Team Lead Iain Fehr  
Front end by Iain Fehr  

1. A **Renpy-based executable file** that hosts the card game in a local sandbox and should be capable of connecting to a hosted server and sending and receiving data from the instance.  
   ***Developed Primarily by Iain Fehr the team leader, all modifications and adaptations have been changed to ensure the game correctly compiles and has local functionality.***  
   
   All  .RPYC files are compiled versions of the same files, they are created when the game is run but can not be read without decompiling them with a tool. 


   Script.rpy -- Starting script for the game, a launch point if you will for the gamefiles  
   Variables.rpy -- Renpy variables stores most game variables not in other documents for accessibility   
   interface.rpy -- Game interface files
   options.rpy -- Game Options
   Network.rpy -- Depreciated and mostly contained within webhook.rpy however provides a fallback
   webhook.rpy -- contains all the server connection code using CORS functions
   gui.rpy -- Game graphical user interface settings 
   _deck_builder_.rpy -- The planned deck builder, some of this works but without assistence I was unable to focus on completing it.
   _card_game_.rpy -- File contains the basic logic for calling and playing the card game
   _card_game_init_.rpy -- Contains the information for the cards, ui element configuration and updating the and playing the game. 
