import socket

def main():
    server_address = ('127.0.0.1', 8889)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect(server_address)

        sock.sendall(b'Hello')

        data = sock.recv(1024)
        print(f"Received response from server: {data.decode()}")

if __name__ == '__main__':
    main()
