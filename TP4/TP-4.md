# TP4 : I'm Socketing, r u soketin ?

## I. Simple bs program

### 1. First steps

🌞 Commandes...

Je veux dans le compte-rendu toutes les commandes réalisées sur le client et le serveur pour que ça fonctionne
et je veux aussi voir une exécution de votre programme
oh et je veux un ss sur le serveur
n'affiche qu'une ligne : celle qui concerne l'écoute de notre programme
ajoutez les bonnes options à ss ainsi qu'un | grep ... pour n'afficher que la bonne ligne.

Server :
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

Client :
```
[lebou@TP4client ~]$ python bs_client_I1.py
Le serveur a répondu 'Salut mec.'
```
```
[lebou@TP4client ~]$ ss -a | grep -i 13337
tcp   TIME-WAIT 0      0                                        10.2.3.4:40398                  10.2.3.3:13337
```