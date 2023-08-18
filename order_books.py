import pickle
import os
from collections import OrderedDict

def create_order_books(order_books, filename):
    with open(filename, "wb") as file:
        pickle.dump(order_books, file)

exchange_folder = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
file_path = os.path.join(exchange_folder, 'order_books.pkl')

bid_side = {
    100:50,
    99:50,
    98:50
}
ask_side = {
    101:50,
    102:50,
    103:50
}
order_books = {
    "asset1": {
        "bid":bid_side,
        "ask":ask_side
    }
}

create_order_books(order_books , file_path)