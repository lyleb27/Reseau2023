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