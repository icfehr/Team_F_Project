init python:
    import requests
    import socket

    SERVER_PORT = 5000  # Define the server port. Ensure this matches your server configuration.

    def get_ip_address_internal():
        """Tries to get a local IP address, preferring non-loopback."""
        default_local_ip = "127.0.0.1"
        try:
            hostname = socket.gethostname()
            # Try getting IP associated with hostname
            ip_address = socket.gethostbyname(hostname)

            # If it's a loopback address, try a more robust method
            if ip_address.startswith("127."):
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.settimeout(0.5)  # Short timeout for local check
                try:
                    # Connect to a well-known external IP (literally googles public DNS)
                    s.connect(('8.8.8.8', 1)) 
                    non_loopback_ip = s.getsockname()[0]
                    if non_loopback_ip and not non_loopback_ip.startswith("127."):
                        ip_address = non_loopback_ip  # Found a better one
                    # else: stick with the ip_address from gethostbyname (which is 127.x)
                except socket.error:
                    # Failed to find a non-loopback via UDP
                    print("Could not determine non-loopback local IP via UDP trick. Using initial local IP or default.")
                finally:
                    s.close()
            return ip_address
        except socket.gaierror: # Error in gethostbyname (e.g. hostname not found)
            print(f"Failed to resolve hostname to IP. Using default local IP: {default_local_ip}")
            return default_local_ip
        except Exception as e: # Catch any other unexpected errors
            print(f"Could not determine local IP address due to an error: {e}. Using default local IP: {default_local_ip}")
            return default_local_ip

    def get_ip():
        # Try to get public IP first
        try:
            # Attempt to fetch public IP using an external service
            response = requests.get("https://api.ipify.org?format=text", timeout=3)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            public_ip = response.text.strip()
            print(f"Successfully fetched public IP: {public_ip}")
            return f"{public_ip}:{SERVER_PORT}"
        except requests.exceptions.Timeout:
            print("Failed to fetch public IP: Request timed out. Falling back to local IP.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to fetch public IP: {e}. Falling back to local IP.")
        except Exception as e: # Catch other  errors
            print(f"An unexpected error occurred while fetching public IP: {e}. Falling back to local IP.")

        # Fallback to local IP if public IP fetching failed
        print("Running in local mode. Network features might be limited to LAN.")
        local_ip = get_ip_address_internal()
        print(f"Using local IP: {local_ip}")
        return f"{local_ip}:{SERVER_PORT}"


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

    def send_board_data(ip_address, player_id, board_state_data):
        """Sends the game board state to the server.
        ip_address should be in 'host:port' format.
        board_state_data should be a 3x3 list of lists, where each cell
        is either None or a dictionary representing a card.
        """
        try:
            payload = {
                "player_id": player_id,
                "board_state": board_state_data
            }
            response = requests.post(f"http://{ip_address}/board_update", json=payload, timeout=5)
            response.raise_for_status()  # Raise an exception for HTTP errors (4xx or 5xx)
            print(f"Successfully sent board state for player {player_id} to {ip_address}.")
            return response.status_code == 200
        except Exception as e:
            print(f"Error sending board state for player {player_id} to {ip_address}: {e}")
            return False

    def test_server_connection():
        """
        Testing the connection to the game server during initialization.
        Tries public/detected IP first, then falls back to localhost.
        Informs the user if multiplayer functionality might be disabled if both fail.
        """
        print("Attempting to connect to the game server...")
        primary_server_address = get_ip() # This already uses SERVER_PORT
        localhost_address = f"127.0.0.1:{SERVER_PORT}"
        server_found = False

        print(f"Attempt 1: Pinging server at {primary_server_address} (obtained via get_ip())...")
        if ping_server(primary_server_address):
            print(f"Successfully connected to the game server at {primary_server_address}. Multiplayer features should be available.")
            server_found = True
        else:
            print(f"Could not connect to server at {primary_server_address}.")
            print(f"Attempt 2: Pinging server at {localhost_address} (localhost fallback)...")
            if ping_server(localhost_address):
                print(f"Successfully connected to the game server at {localhost_address}. Multiplayer features should be available (local server).")
                server_found = True

        if not server_found:
            print(f"Could not connect to the game server at {primary_server_address} or {localhost_address}. Multiplayer functionality will be disabled. Please ensure the server is running and accessible on port {SERVER_PORT}.")

# Run the server connection test during a later init phase
init 10 python:
    test_server_connection()
