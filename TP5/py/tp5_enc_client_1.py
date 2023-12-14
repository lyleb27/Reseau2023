import socket 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('127.0.0.1', 9999))

expression = input('Enter a simple arithmetic expression (Do not forget the spaces, example (3 + 3)): ')
try:
    x, operator, y = map(str.strip, expression.split())
    x = int(x)
    y = int(y)
except ValueError:
    print("Invalid input. Please enter a valid arithmetic expression.")
    sock.close()
    exit()

if not 0 <= x <= 4294967295 or not 0 <= y <= 4294967295:
    print("Numbers should be within the range [0, 4294967295].")
    sock.close()
    exit()

x_bytes = x.to_bytes(4, byteorder='big')
y_bytes = y.to_bytes(4, byteorder='big')
operator_byte = operator.encode('utf-8')

total_size = len(x_bytes) + len(operator_byte) + len(y_bytes)

header = total_size.to_bytes(4, byteorder='big')

payload = header + x_bytes + operator_byte + y_bytes

sock.send(payload)

sock.close()
