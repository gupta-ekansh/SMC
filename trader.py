# Importing requirements
import socket
import pickle

# Configure trader settings
SERVER_IP = socket.gethostname()  # Replace with the exchange's IP address
SERVER_PORT = 12345   # Replace with the exchange's port

# Connecting to exchange server
def send_trade_request(trade_data):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        serialized_data = pickle.dumps(trade_data)
        client_socket.sendall(serialized_data)

        response = client_socket.recv(1024).decode()
        print("Server response:", response)

# Simulate trader sending a trade request
trade_data = {
    "oid":1,               # OrderId
    "asset_id": "asset1",  # AssetId
    "quantity":50,         # Quantity of the asset
    "price":97.5,          # Price of the asset
    "buy_signal": 0,       # 1 to buy 0 to sell
    "request_no":3         # 1 for new , 2 for modify , 3 for cancel
}

# Function to send data to server
send_trade_request(trade_data)