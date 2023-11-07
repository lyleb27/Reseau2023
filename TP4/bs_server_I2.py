import socket

IP_SERVER = "10.2.3.3"
PORT = 13337

def handle_message(client_socket, client_address, message):
    print(f"Message reçu de {client_address}: {message}")

    if "meo" in message:
        response = "Meo à toi confrère."
    elif "waf" in message:
        response = "ptdr t ki"
    else:
        response = "Mes respects humble humain."

    client_socket.send(response.encode())

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((IP_SERVER, PORT))
    server_socket.listen(5)
    print(f"Le serveur est à l'écoute sur {IP_SERVER}:{PORT}")

    response_count = 0
    while response_count < 3:
        client_socket, client_address = server_socket.accept()
        print(f"Un client vient de se co et son IP c'est {client_address[0]}.")

        message = client_socket.recv(1024).decode()
        handle_message(client_socket, client_address, message)
        client_socket.close()
        response_count += 1

if __name__ == "__main__":
    main()

