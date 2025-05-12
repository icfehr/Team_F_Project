### 2025S_CSCI441_VA_Software Engineering
### Team_F_Project
### Card Game

Front end by Iain Fehr

1. A **Renpy-based executable file** that hosts the card game in a local sandbox and should be capable of connecting to a hosted server and sending and receiving data from the instance. 
   ***Developed Primarily by Iain Fehr the team leader, all modifications and adaptations have been changed to ensure the game correctly compiles and has local functionality.***

   THIS FILE IS LOCATED IN THE LOCAL_LAUNCHER FOLDER
   THE GAME FILES ARE SPLIT INTO A RAW DECOMPILED VERSION OF THE GAME FOR FILE ACCESS AND A COMPILED VERSION UNDER THE PROJECT F FOLDER THAT CONTAINS AND EXE

    Decompiled:
    /RAW/Scripts -- Code 
    /RAW/gui -- Renpy native GUI images
    /RAW/images -- Images directory within Renpy contains project images and UI images
    /RAW/saves -- Unused as game supports saving but is unneeded for use case
    /RAW/audio -- Unused 
    /RAW/cache -- Unused would be possible to store persistent variable like player stats inside.

    .rpy files are readable 
    .rpyc files are unreadable files as they are compiled on game launch

    A).
    To run game navigate to /Project_F/game.exe 
    launch game 

    B).
    Self Compilation of game files 
    1. Download the Renpy SDK HTML: https://www.renpy.org/latest.html 
    2. Extract the SDK 
    3. Clone the repository within the default directory of where you extracted the SDK 
    4. Ensure Renpy sees the cloned project files and change the directory of where the project is located if placed in a different directory 
    5. Launch the game from SDK

