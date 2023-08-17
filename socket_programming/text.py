with open('compressed_data.hex' , 'r') as file:
    hex_data = file.read().replace('\n' , '')

binary_data = bytes.fromhex(hex_data)

with open('compressed_data.bin' , 'wb') as file:
    file.write(binary_data)