import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9999))
sock.listen()
client, client_addr = sock.accept()

while True:
    header = client.recv(4)
    if not header:
        break

    msg_len = int.from_bytes(header, byteorder='big')

    print(f"Reading the next {msg_len} bytes")

    chunks = []

    bytes_received = 0
    while bytes_received < msg_len:
        chunk_size = min(msg_len - bytes_received, 1024)
        chunk = client.recv(chunk_size)
        if not chunk:
            raise RuntimeError('Invalid chunk received')

        chunks.append(chunk)

        bytes_received += len(chunk)

    message_received = b"".join(chunks).decode('utf-8')

    if message_received.endswith("<clafin>") or message_received.endswith("0"):
        x = int.from_bytes(message_received[0:4], byteorder='big')
        operator = message_received[4]
        y = int.from_bytes(message_received[5:], byteorder='big')

        # Perform the calculation based on the operator
        if operator == '+':
            result = x + y
        elif operator == '-':
            result = x - y
        elif operator == '*':
            result = x * y
        else:
            print("Invalid operator.")
            continue

        print(f"Received from client: {x} {operator} {y} = {result}")
    else:
        print("Invalid message format. Ending sequence not found.")

client.close()
sock.close()
