### 2025S_CSCI441_VA_Software Engineering  
### Team_F_Project  
### Card Game  
  
# Ren'Py Card Game with Flask Backend  
  
This Project is split into 2 parts:
1. A **Renpy-based executable file** that hosts the card game in a local sandbox and should be capable of connecting to a hosted server and sending and receiving data from the instance.  
  
    Developed Primarily by Iain Fehr the team leader, all modifications and adaptations have been changed to ensure the game correctly compiles and has local functionality.  
  
    Current Features:  
        Ability to compile the game and start it (harder than it sounds)  
        Pings internet to acquire the outward ip address of the local network  
        Local Card Game Functionality correctly working  
        50+ art assets from Juan  
        Ability to ping server for future multiplayer connection  
        Accurate card updates and correct image sizing based on dynamic scaling  
    Abandoned Features  
        Deck builder -- needed menu and art assets current replacement plan is to implement a random deck function to allow for repeatable gameplay  
        Player Stats tracking -- Needed menu and art assets  
        A replayable function instead of the demo function needed art asset  
        True tested working multiplayer -- current functionality pushes an update to the server but without another player is unable to test functionality of receiving a push from the server using await  
  
  
  
2. A **Flask-based web application** that simulates a simple card game with multi-player support and move history tracking. It features a backend to manage game data and an admin panel to view the results.  
    Current Features:  
        Lightweight database intended to track moves that can recieve push requests from the local game clients(intended to prevent cheating on large scale deployments)  
        Flask based infrastructure designed for ease of development  
        Based in python for ease of connectivity toward the game engine  
        Local host development mode for connectivity development testing  
        Replay history (partially implemented due to recent changes on local game files) intened to allow for cloud replay and rematching of games  
        Theoretically capable of mirroring and doing gameplay on the server itself  
    Abandoned features  
        A multiplayer matchmaking service -- potentially random skill based match making unavailable due to player Stats tracking inoperable  
  
  
FILES AND FILE STRUCTURE  
  
CODE -- Where the game files are located  
    /code/Flask_Server_backend/ -- Where the games server project files are held see server readme for more details on installation and running within a local environment  
    /code/Local_Launcher/ -- Where the renpy executable files are held,  these are nicely organized within the game folder when compiled The project F folder holds a compiled version with an executable as gamefiles  are formatted in machine code by default without being decompiled.  
    /code/Local_Launcher/Project_F -- will hold a compiled version  
    /code/Local_Launcher/Raw -- will hold a decompiled version that can be used to reference the internal code.  
  
  
DOC -- Documentation and Project files used to plan and create the project
    DOC/Demo 1 holds the powerpoint and images used within the first video demonstration  
    Report #1 -- Holds the original files submitted and the origninal plan for the project  
    Report #2 -- Holds the original files submitted and original updated plan for the project deployment  
    Report #3 -- holds relatively up to date information on how the project should and has been implemented  
    DOC/Demo 2/ Holds the powerpoint and images used within the second video demonstration  

DESIGN -- Holds the images used in report 3 and are a example of the UML Diagrams planned for the project  
    Note these images are not 100% accurate due to constraints around individuals participating in the project  

DATA -- Only used for reference as all images are required to be within the project files for the game to compile correctly.  
    All images are held within a mirror of the games own file structure  

Unused and Removed:  
  
TESTS -- Initially intended for testing features, proved to be redundant as Renpy's inbuilt compiler includes testing functionality in engine and will not compile if an error occurs while giving an accurate trackback
    ---Integration tests unable to be completed due to being assigned to no show members  



