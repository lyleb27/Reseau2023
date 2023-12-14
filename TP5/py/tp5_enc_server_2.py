import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('127.0.0.1', 9999))
sock.listen()
client, client_addr = sock.accept()

while True:
    # Read the 4-byte header from the client
    header = client.recv(4)
    if not header:
        break

    # Read the message size
    msg_len = int.from_bytes(header, byteorder='big')

    print(f"Reading the next {msg_len} bytes")

    # A list to store received data
    chunks = []

    bytes_received = 0
    while bytes_received < msg_len:
        # If we receive more than the announced size, read 1024 bytes at a time
        chunk_size = min(msg_len - bytes_received, 1024)
        chunk = client.recv(chunk_size)
        if not chunk:
            raise RuntimeError('Invalid chunk received')

        # Add the chunk of 1024 bytes or less to our list
        chunks.append(chunk)

        # Update the byte counter with the received bytes
        bytes_received += len(chunk)

    # Assemble the list into a single message
    message_received = b"".join(chunks).decode('utf-8')

    # Check if the message ends with the specified sequence
    if message_received.endswith("<clafin>0"):
        # Extract operands and operator from the message
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
