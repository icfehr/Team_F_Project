### 2025S_CSCI441_VA_Software Engineering
### Team_F_Project
### Card Game

Backend by Angel 
Readme Written by Iain

**Flask-based Server Installation Instructions** 
Intended to simulates a simple card game with multi-player support and move history tracking. It features a backend to manage game data and an admin panel to view the results. 

## Getting Started
   

   Flask Backend
      **Requirements**

      Precursor Python 3 must be installed on the system to host the backend server files
      BASH must be installed to install system requirements.txt 
      User might have to configure port settings for multiplayer functionality over PTP or internet functionality, contact your network administrator for permissions if you are unable to change your system and local network settings.  

      ### Installation
      Clone the Project Repository from GitHub

      if BASHE in installed run the following command 
      ```
      git clone https://github.com/yourusername/renpy-cardgame-server-template.git
      ```

      Otherwise download the repo from this link:
      Repository URL https://github.com/icfehr/Team_F_Project

      1. Open a terminal in `flask_backend/` or Navigate to `flask_backend/` in an existing terminal

      2. Execute this command line block to install the requirements for the server host application:
         ```
         pip install -r ../requirements.txt
         ```
      3.
         After the requirements have been successfully run the following code in the terminal to start the server:
         ```
         python app.py
         ```
      4. If the server has started correctly then it should be running locally on the address 127.0.0.1 using port 5000.



