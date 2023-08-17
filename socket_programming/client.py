import socket
import struct
import pickle 
import time
import sys
def client_program(received_data):
    # host = '192.168.15.241'
    host = '233.1.2.5'
    port = 34842

    client_socket = socket.socket()  
    client_socket.connect((host, port))  

    buffer_size = 1024
    partial_data = b""
    data_chunk = client_socket.recv(buffer_size)
    received_data += data_chunk
#     # received_data = []
#     i=0
#     with open('sample.txt', 'w') as file:
#         while True:
#             data_chunk = client_socket.recv(buffer_size)
#             data_chunk = partial_data + data_chunk

#             while len(data_chunk) >= 516:
#                 file.write(str(data_chunk[:516]) + "\n")
#                 received_data.append(data_chunk[:516])
#                 data_chunk = data_chunk[516:]
        
#             partial_data = data_chunk

#             if b"Terminate" in data_chunk:
#                 break

#     # print(len(received_data))
#     # print(received_data)  
#     print("Received")
#     client_socket.close() 
#     # with open('sample.txt' , 'w') as file:
#     #     file.write(str(data_chunk))

# def read_data_from_file(file_path):
#     with open(file_path, 'r') as file:
#         data_str = file.readline().strip()

#     data_bytes = eval(data_str)
#     # print(data_bytes)
#     format_string = '=2sh512s'
#     data_length = struct.calcsize(format_string)
#     print(data_length)
#     unpacked_data = []

#     for i in range(0, len(data_bytes), data_length):
#         unpacked_set = struct.unpack(format_string, data_bytes[i:i+data_length])
#         unpacked_data.append(unpacked_set)

#     return unpacked_data


if __name__ == '__main__':
    received_data = []
    client_program(received_data)
    # print(received_data)
    print(len(received_data))

    # unpacked_data = read_data_from_file(b"".join(received_data))

    # file_path = 'sample.txt'
    # data = read_data_from_file(file_path)     
    # for i,set_data in enumerate(data):        
    #     print("Set", i + 1)                   
    #     print("Msg_length:", set_data[0])     
    #     print("home_team_goals:", set_data[1])
    #     print("away_team_goals:", set_data[2])
        # print("home_team_saves:", set_data[3])
        # print("away_team_saves:", set_data[4])
        # print("home_team_fouls:", set_data[5])
        # print("away_team_fouls:", set_data[6])