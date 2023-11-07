import socket

host = '10.2.3.3'
port = 13337


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))  

s.listen(1)
conn, addr = s.accept()
print(f"Un client vient de se co et son IP c'est {addr}.")

while True:

    try:
        data = conn.recv(1024).decode('utf-8')
        
        if not data: break
        
        print(f"Données reçues du client : {data}")

        message = "Will be send to the client"
        if "meo" in data :
            message = "Meo à toi confrère."
        elif "waf" in data :
            message = "ptdr t ki"
        else :
            message = "Mes respects humble humain."
        conn.sendall(message.encode('utf-8'))
    except socket.error:
        print("Error Occured.")
        break

conn.close()


