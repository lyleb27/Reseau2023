import socket
import struct

host = 'localhost'
port = 12345

number_to_send = 100000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((host, port))

    data_to_send = struct.pack('!I', number_to_send)

    client_socket.sendall(data_to_send)

    print(f"Nombre {number_to_send} envoyé au serveur")
