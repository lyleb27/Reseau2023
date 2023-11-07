import logging
import socket
import time

logging.basicConfig(filename='/var/log/bs_server/bs_server.log', level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s %(message)s')
console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
logging.getLogger('').addHandler(console)

def log_server_start(ip, port):
    logging.info(f"Le serveur tourne sur {ip}:{port}")

def log_client_connect(client_ip):
    logging.info(f"Un client {client_ip} s'est connecté.")

def log_received_message(client_ip, message):
    logging.info(f"Le client {client_ip} a envoyé : {message}.")

def log_sent_message(client_ip, message):
    logging.info(f"Réponse envoyée au client {client_ip} : {message}.")

def log_no_clients_connected():
    logging.warning("Aucun client depuis plus d'une minute.")

def main():
    host = '10.2.3.3'
    port = 13337
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    log_server_start(host, port)

    # Code du serveur

if __name__ == "__main__":
    main()
