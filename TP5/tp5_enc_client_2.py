import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))

# Get user input for a simple arithmetic expression
try:
    x = int(input('Enter the first integer: '))
    operator = input('Enter the operator (+, -, *): ')
    y = int(input('Enter the second integer: '))
except ValueError:
    print("Invalid input. Please enter valid integers.")
    sock.close()
    exit()

# Check if numbers are within the allowed range
if not 0 <= x <= 4294967295 or not 0 <= y <= 4294967295:
    print("Numbers should be within the range [0, 4294967295].")
    sock.close()
    exit()

# Convert operands and operator to bytes
x_bytes = x.to_bytes(4, byteorder='big')
y_bytes = y.to_bytes(4, byteorder='big')
operator_byte = operator.encode('utf-8')

# Calculate the total payload size
total_size = len(x_bytes) + len(operator_byte) + len(y_bytes)

# Create the header with the total size
header = total_size.to_bytes(4, byteorder='big')

# Concatenate the header, operands, and operator
payload = header + x_bytes + operator_byte + y_bytes

# Send the payload to the server
sock.send(payload)

# Send the ending sequence to indicate the completion of the message
sock.send("<clafin>0".encode('utf-8'))

# Close the socket
sock.close()
