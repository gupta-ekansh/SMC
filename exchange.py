import socket
import pickle
import os
from collections import OrderedDict

def save_order_books(order_books, filename):
    with open(filename, "wb") as file:
        pickle.dump(order_books, file)

def load_order_books(filename):
        with open(filename, "rb") as file:
            return pickle.load(file)

def execute_trade(asset_id , quantity , price , file_path, buy_signal):
        order_books = load_order_books(file_path)
        print("OrderBookBefore:" , order_books)
        if asset_id in order_books and "bid" in order_books[asset_id] or "ask" in order_books[asset_id]:
            if buy_signal:
                ask_side = order_books[asset_id]["ask"]
                bid_side = order_books[asset_id]["bid"]
                remaining_quantity = quantity

                for ask_price, ask_quantity in list(ask_side.items()):
                    if remaining_quantity == 0:
                        break

                    if ask_price <= price:
                        traded_quantity = min(ask_quantity, remaining_quantity)
                        remaining_quantity -= traded_quantity
                        ask_quantity -= traded_quantity

                        if ask_quantity == 0:
                            del ask_side[ask_price]
                        else:
                            ask_side[ask_price] = ask_quantity
                if remaining_quantity > 0:
                    if price not in bid_side:
                        bid_side[price] = 0
                    bid_side[price] += remaining_quantity

                    order_books[asset_id]["bid"] = dict(sorted(bid_side.items(), key=lambda item: item[0] ,reverse=True))
            else:
                bid_side = order_books[asset_id]["bid"]
                ask_side = order_books[asset_id]["ask"]
                remaining_quantity = quantity

                for bid_price, bid_quantity in list(bid_side.items()):
                    if remaining_quantity == 0:
                        break

                    if bid_price >= price:
                        traded_quantity = min(bid_quantity, remaining_quantity)
                        remaining_quantity -= traded_quantity
                        bid_quantity -= traded_quantity

                        if bid_quantity == 0:
                            del bid_side[bid_price]
                        else:
                            bid_side[bid_price] = bid_quantity
                if remaining_quantity > 0:
                    if price not in ask_side:
                        ask_side[price] = 0
                    ask_side[price] += remaining_quantity

                # Sort the ask side based on price
                order_books[asset_id]["ask"] = dict(sorted(ask_side.items(), key=lambda item: item[0]))
                # print(sorted_ask_side)
                # Update the order book
            print("OrderBookAfter:" , order_books)
            save_order_books(order_books, file_path)

            return remaining_quantity

def handle_client_request(client_socket , request_data , file_path):
    asset_id = request_data["asset_id"]
    quantity = request_data["quantity"]
    price = request_data["price"]
    buy_signal = request_data["buy_signal"]

    if not buy_signal:
        remaining_quantity = execute_trade(asset_id, quantity, price , file_path,buy_signal)
        response = f"Trade executed. Remaining quantity: {remaining_quantity}"
    else:
        remaining_quantity = execute_trade(asset_id, quantity, price , file_path,buy_signal)
        response = f"Sell trade executed. Remaining quantity: {remaining_quantity}"

    client_socket.sendall(response.encode())

# Configure server settings
HOST = '192.168.15.237'  # Listen on all available interfaces
# HOST = '0.0.0.0'
PORT = 12345     # Choose a suitable port number

# Create a socket server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()

    exchange_folder = os.path.dirname(os.path.abspath(__file__)) 
    file_path = os.path.join(exchange_folder, 'order_books.pkl')

    print("Exchange is listening for connections...")
    while True:
        conn, addr = server_socket.accept()

        with conn:
            print(f"Connected by: {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                request_data = pickle.loads(data)
                print("Request Data:", request_data)
                handle_client_request(conn , request_data , file_path)