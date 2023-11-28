# TP5 : Coding Encoding Decoding

## I. Jouer avec l'encodage
CLIENT :

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


SERVER : 

import socket
import struct

host = 'localhost'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((host, port))
    
    server_socket.listen()

    print(f"Le serveur écoute sur {host}:{port}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connecté par {addr}")

        data = conn.recv(4)  # Nous recevons 4 octets pour représenter l'entier (32 bits)
        if not data:
            print("Aucune donnée reçue")
        else:
            number = struct.unpack('!I', data)[0]
            print(f"Nombre reçu : {number}")


## II. Opti calculatrice




