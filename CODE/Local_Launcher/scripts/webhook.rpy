init python:
    import requests

    def get_ip():
        return "192.168.1.122:5000"  # your server's IP + port

    def ping_server(ip):
        try:
            response = requests.get(f"http://{ip}/ping")
            return response.status_code == 200 and response.json().get("status") == "ok"
        except:
            return False

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
        try:
            response = requests.get(f"http://{ip}/opponent")
            if response.status_code == 200:
                data = response.json()
                return data.get("player_id"), data.get("player_name")
            return None, None
        except:
            return None, None

    def send_move(ip, player_id, move_data):
        try:
            data = {
                "player_id": player_id,
                "move": move_data
            }
            response = requests.post(f"http://{ip}/move", json=data)
            return response.status_code == 200
        except:
            return False

    def get_latest_move(ip):
        try:
            response = requests.get(f"http://{ip}/latest_move")
            if response.status_code == 200:
                return response.json().get("move")
            return None
        except:
            return None
