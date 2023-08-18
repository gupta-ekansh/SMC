import socket
import pickle

# Configure trader settings
SERVER_IP = socket.gethostname()  # Replace with the exchange's IP address
SERVER_PORT = 12345   # Replace with the exchange's port

def send_trade_request(trade_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        serialized_data = pickle.dumps(trade_data)
        client_socket.sendall(serialized_data)

        response = client_socket.recv(1024).decode()
        print("Server response:", response)

# Simulate trader sending a trade request
trade_data = {
    "asset_id": "asset1",
    "quantity": 98.5,
    "price":200,
    "buy_signal": 0
}

send_trade_request(trade_data)