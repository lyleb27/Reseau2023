# TP4 : I'm Socketing, r u soketin ?

## I. Simple bs program

### 1. First steps

🌞 Commandes...

Server : [bs_server_I1.py](/TP4/bs_server_I1.py)
```
[lebou@TP4server ~]$ sudo firewall-cmd --add-port=13337/tcp --permanent
success
[lebou@TP4server ~]$ sudo firewall-cmd --reload
success
```

```
[lebou@TP4server ~]$ python bs_server_I1.py
b'Hi mate !'
Données reçues du client : Meooooo !
```

Client : [bs_client_I1.py](/TP4/py/bs_client_I1.py)
```
[lebou@TP4client ~]$ python bs_client_I1.py
Le serveur a répondu 'Salut mec.'
```

```
[lebou@TP4client ~]$ ss -a | grep -i 13337
tcp   TIME-WAIT 0      0                                        10.2.3.4:40398                  10.2.3.3:13337
```
### 2. User friendly

🌞 [bs_client_I2.py](/TP4/py/bs_client_I2.py)

```
[lebou@TP4client ~]$ python bs_client_I1.py
Connecté avec succès au serveur 10.2.3.3 sur le port 13337
Que veux-tu envoyer au serveur : je suis humain
Réponse du serveur : Mes respects humble humain.
Que veux-tu envoyer au serveur : meo
Réponse du serveur : Meo à toi confrère.
Que veux-tu envoyer au serveur : waf
Réponse du serveur : ptdr t ki
```

🌞 [bs_server_I2.py](/TP4/py/bs_server_I2.py)

```
[lebou@TP4server ~]$ python bs_server_I1.py
Un client vient de se co et son IP c'est ('10.2.3.4', 41406).
Données reçues du client : je suis humain
Données reçues du client : meo
Données reçues du client : waf
```

### 3. You say client I hear control
🌞 [bs_client_I3.py](/TP4/py/bs_client_I3.py)

```

```

## II. You say dev I say good practices
### 1. Args

🌞 [bs_server_II1.py](/TP4/py/bs_server_II1.py)

```
[lebou@TP4server ~]$ python bs_server_II1.py -p 8888
Serveur en cours d'exécution sur le port 8888
[lebou@TP4server ~]$ python bs_server_II1.py -p 655354
ERROR: Le port spécifié n'est pas un port possible (de 0 à 65535).
[lebou@TP4server ~]$ python bs_server_II1.py -p 1024
ERROR: Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.
[lebou@TP4server ~]$ python bs_server_II1.py -h
usage: bs_server_II1.py [-h] [-p PORT]

Simple server with port configuration.

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Port number to listen on. Must be between 0 and 65535.
```

### 2. Logs

🌞 [bs_server_II2A.py](/TP4/py/bs_server_II2A.py)

Pour créer le fichier bs_server.log :
```
[lebou@TP4server ~]$ sudo mkdir -p /var/log/bs_server
[lebou@TP4server ~]$ sudo touch /var/log/bs_server/bs_server.log
[lebou@TP4server ~]$ sudo chown lebou /var/log/bs_server/bs_server.log
```


### B. Logs client

🌞 [bs_client_II2B.py](/TP4/py/bs_client_II2B.py)

```

```