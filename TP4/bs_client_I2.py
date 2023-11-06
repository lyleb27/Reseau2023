import socket
import sys

# On définit la destination de la connexion
host = '10.2.3.3'  # IP du serveur
port = 13337  # Port choisir par le serveur

# Création de l'objet socket de type TCP (SOCK_STREAM)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connexion au serveur
s.connect((host, port))

# Envoi de data bidon
s.sendall('Meooooo !'.encode('utf-8'))

# On reçoit 1024 bytes qui contiennent peut-être une réponse du serveur
data = s.recv(1024).decode('utf-8')

# On libère le socket TCP
s.close()

# Affichage de la réponse reçue du serveur
print(f"Le serveur a répondu {repr(data)}")

# Quitte proprement avec un code de retour 0
sys.exit(0)