# renpy_integration/network.rpy

init python:
    import sys

    # Join the game
    def join_game(player_name):
        if not requests:
            return "Requests module not available. Cannot join game."
        url = "http://127.0.0.1:5000/join"
        response = requests.post(url, json={"player": player_name})  # fixed key
        if response.status_code == 200:
            renpy.pause(1, hard=True)
            return response.json().get('message', 'No message from server')
        else:
            return "Failed to join game"

    # Update player stats
    def update_player_stats(player_name, wins, losses, score):
        if not requests:
            return "Requests module not available. Cannot update stats."
        url = "http://127.0.0.1:5000/update_player"
        data = {
            "player": player_name,  # fixed key
            "wins": wins,
            "losses": losses,
            "score": score
        }
        response = requests.post(url, json=data)
        if response.status_code == 200:
            renpy.pause(1, hard=True)
            return response.json().get('message', 'No message from server')
        else:
            return "Failed to update stats"

    # Get game state
    def get_game_state():
        if not requests:
            return "Requests module not available. Cannot get game state."
        url = "http://127.0.0.1:5000/game_state"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json().get('players', [])
        else:
            return []

    # Get IP address
    def get_ip():
        try:
            # Fetch the public IP address using an external service
            response = requests.get("https://api.ipify.org?format=text")
            if response.status_code == 200:
                return response.text
            else:
                return "Unknown IP Failed to fetch IP address"
        except:
            return "Unknown IP Failed to fetch IP address"

    ### Placeholder for pinging game server for connection availability
    def ping_server(ip):
        try:
            response = requests.get(f"http://{ip}/ping")
            if response.status_code == 200:
                return response.json().get("status") == "ok"
                
            else:
                return excecpt("Server not reachable")
                

        except:
            return False
    
    ### Send Player data to the server
    def send_player_data(ip, player_id, player_name):
        try:
            data = {
                "player_id": player_id,
                "player_name": player_name

            }
            response = requests.post(f"http://{ip}/register", json=data)
            return response.status_code == 200
        except:
            return False

    def receive_opponent_data(ip):
        """
        Fetch the opponent player's data (player_id and player_name) from the server.
        """
        try:
            response = requests.get(f"http://{ip}/opponent")
            if response.status_code == 200:
                data = response.json()
                opponent_id = data.get("player_id")
                opponent_name = data.get("player_name")
                return opponent_id, opponent_name
            else:
                return None, None
        except:
            return None, None