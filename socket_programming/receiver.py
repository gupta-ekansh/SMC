import socket
import struct
from multiprocessing import Process
import time
import zlib
import lzo
import lzma
import bz2
import pylzma
import lz4.frame
import subprocess
# def get_interfaces():
#     interfaces = socket.getaddrinfo(socket.gethostname(), None)
#     return {addr[4][0]: addr[1] for addr in interfaces}
def receive_and_append_data(filename,max_iterations=1):
    multicast_group = '233.1.2.5'  
    multicast_port = 34330  

    interface_ip = '10.10.10.103'

    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    sock.bind((interface_ip, multicast_port))


    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, socket.inet_aton(multicast_group) + socket.inet_aton(interface_ip))

    print(f"Listening for NSE snapshot data on {multicast_group}:{multicast_port}")

    i = True
    while True:
        try:
                with open('sample.txt' , 'a') as file:
                    # iteration = 0
                    # while iteration < max_iterations:
                        data, address = sock.recvfrom(4096)
                        print(f"Received data from {address}: {len(data)}")
                        # print(data_compressed)
                        file.write(str(data) + "\n")
                        # print("data written in file")
                        decode_data(data, i)
                        i = i + 1
                        time.sleep(1)
                        # decode_data('sample.txt')
                        # iteration += 1
        except socket.error as e:
                print(f"Error receiving data: {e}")
                i = False
    
    # finally:
    #     sock.close()

def decode_data(data , i):
    # with open(filename , 'r') as file:
    #     data = file.read().encode('utf-8')

    # data = eval(data)
    with open('output.txt' , 'a') as file:
        # print(data)
        first = data[:4]


        # print("data decoded")

        # for i in range(15):
        #       broadcast_data = data[i:]
        #       try:
        #             decompressed_data = lzo.decompress(broadcast_data)
        #       except:
        #             print("error")
        # print(first)
        a,b = struct.unpack('=2sh' , first)
        a = a[0]
        stri = "Set no.: " + str(i) + " cNetId:" + str(a)+ " iNoPackets:" + str(b) + "\n"
        # a = a.encode()
        file.write(stri)
        

    # print(char_arr)
    # print(short_var)
    
    # character_array, short_variable = struct.unpack('=2sh', data_stream_string)
    # print("Character array as bytes:", character_array)
    # print("Short variable:", short_variable)

if __name__ == "__main__":
    filename = "sample.txt"
    max_iterations = 1
    i = 1
    # p1 = Process(target = receive_and_append_data(filename , max_iterations))
    # p1.start
    # p2 = Process(decode_data(filename))
    # p2.start
    receive_and_append_data(filename , max_iterations)