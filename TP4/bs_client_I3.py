import socket
import re
 
host = '10.2.3.3'
port = 13337

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
    print(f"Connecté avec succès au serveur {host} sur le port {port}")
except TypeError:
    print("Sa marche pô, déso.")
    exit(2)

message = input("Que veux-tu envoyer au serveur : ")

if type(message) is not str :
    s.close()
    raise TypeError("Dialecte primaire non compris.")
        
 
if not re.match(r"^(?!(?=.*waf)(?=.*meo)).*$", message):
    s.close()
    raise ValueError("Suspicion de tentative d'infiltration.")
    
s.sendall(message.encode('utf-8'))

data = s.recv(1024).decode('utf-8')

print(f"Le serveur a répondu {repr(data)}")
s.close()
