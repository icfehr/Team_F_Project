### 2025S_CSCI441_VA_Software Engineering
### Team_F_Project
### Card Game




# Ren'Py Card Game with Flask Backend

This Project is split into 2 parts:
1. A Renpy-based executable file that hosts the card game in a local sandbox and should be capable of connecting to a hosted server and sending and receiving data from the instance. 

2. A **Flask-based web application** that simulates a simple card game with multi-player support and move history tracking. It features a backend to manage game data and an admin panel to view the results. 

### Features:
- **Start the Game**: Deal cards to players and start the game.
- **Play Card**: Players can play cards, and the game updates the hand.
- **Move History**: All game moves are tracked in a database.
- **Admin Panel**: View all game moves, player actions, and timestamps.
- **Multi-Player Support**: Allows for multi-player games (work in progress).
- **Win/Loss Tracking**: Results are tracked and stored (work in progress).
- **Ability to connect to the Renpy game instance for ease of use on multiple platforms

### Potential Future Features
- *** Verifying Connection of  local executable files in difference instances to the flask to enable multiplayer experiences
- *** Real-time connection using the server as an IP address shield or potentially PTP connections 
- ** Adding Ai opponents to a local sandbox when multiplayer functionality is unavailable
- ** A total of 20 cards instead of the six currently in the game in both player's colors and player avatars
- ** Continuous evaluations of the game environment for implementation of known algorithms to speed up runtime

## Getting Started
   
   LOCAL INSTANCE
   Renpy Local Environment (Current -- See Planned Features for Final Release) 
   
   Executable File
   A(1). 
      1. Download Project files and Lanuch Renpy Exe file to start game
   
   Self Compilation of game files
   A(2).
      1. Download the Renpy SDK
           HTML: https://www.renpy.org/latest.html
      2. Extract the SDK
      3. Clone the repository within the default directory of where you extracted the SDK
      4. Ensure Renpy sees the cloned project files and change the directory of where the project is located if placed in a different directory
      5. Launch the game from SDK

   B. Flask Backend
      Requirements
      Precursor Python 3 must be installed on the system to host the backend server files
      BASH must be installed to install system requirements 
      User might have to configure port settings for multiplayer functionality over PTP or internet functionality, contact your network administrator for permissions if you are unable to change your system and local network settings.  

      1. Navigate to `flask_backend/`
      2. Run:
         ```bash
         pip install -r ../requirements.txt
         python app.py
      ```
      code blocks for commands
      ```
      
      ### Installation
      
      1. **Clone the repository**:
         Run the BASH command 
         ```bash
         git clone https://github.com/yourusername/renpy-cardgame-server-template.git
         cd renpy-cardgame-server-template
