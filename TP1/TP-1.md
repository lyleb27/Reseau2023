# TP1 : Maîtrise réseau du poste

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

- l'adresse MAC de votre carte WiFi
- l'adresse IP de votre carte WiFi
- le masque de sous-réseau du réseau LAN auquel vous êtes connectés en WiFi
  - en notation CIDR, par exemple `/16` : 192.168.72.192/24
  - ET en notation décimale, par exemple `255.255.0.0`
```
Adresse physique . . . . . . . . . . . : 40-23-43-62-DB-DD
Adresse IPv4. . . . . . . . . . . . . .: 192.168.72.192
Masque de sous-réseau. . . . . . . . . : 255.255.255.0
```

- l'adresse de réseau du LAN auquel vous êtes connectés en WiFi : 192.168.72.192
- l'adresse de broadcast : 192.168.72.255
- le nombre d'adresses IP disponibles dans ce réseau : 254
- déterminer le hostname de votre PC :
```
PS C:\Users\lebou> hostname
LAPTOP-R8S29PG0
```
- l'adresse IP de la passerelle du réseau
- l'adresse MAC de la passerelle du réseau
```
 Adresse Internet      Adresse physique      Type
  192.168.72.5          da-6d-93-62-07-09     dynamique
```
- l'adresse IP du serveur DHCP qui vous a filé une IP
- l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet
```
Serveur DHCP . . . . . . . . . . . . . : 192.168.72.5
Serveurs DNS. . .  . . . . . . . . . . : 192.168.72.5
```
- dans votre table de routage, laquelle est la route par défaut
``` 
  IPv4 Table de routage
===========================================================================
Itinéraires actifs :
Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
          0.0.0.0          0.0.0.0     192.168.72.5   192.168.72.192     55
```

# II. Go further

- faites en sorte que pour votre PC, le nom `b2.hello.vous` corresponde à l'IP `1.1.1.1`
- prouvez avec un `ping b2.hello.vous` que ça ping bien `1.1.1.1`
```
PS C:\Windows\System32\drivers\etc> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=286 ms TTL=56
Réponse de 1.1.1.1 : octets=32 temps=21 ms TTL=56
Réponse de 1.1.1.1 : octets=33 temps=22 ms TTL=56

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 3, reçus = 3, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 21ms, Maximum = 286ms, Moyenne = 109ms
```
- l'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo
- le port du serveur auquel vous êtes connectés
- le port que votre PC a ouvert en local pour se connecter au port du serveur distant


Déterminer...

- à quelle adresse IP correspond le nom de domaine `www.ynov.com`

```
PS C:\Users\lebou> nslookup www.ynov.com
Serveur :   lanspeedtest.wifirst.fr
Address:  10.188.0.1

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          2606:4700:20::ac43:4ae2
          172.67.74.226
          104.26.10.233
          104.26.11.233
```

- à quel nom de domaine correspond l'IP `174.43.238.89`

```
PS C:\Users\lebou> nslookup 174.43.238.89
Serveur :   lanspeedtest.wifirst.fr
Address:  10.188.0.1

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

- par combien de machines vos paquets passent quand vous essayez de joindre `www.ynov.com`

``

PS C:\Users\lebou> tracert -4 www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.11.233]
avec un maximum de 30 sauts :

  1     2 ms     1 ms     1 ms  lanspeedtest.wifirst.fr [10.188.0.1]
  2     *        2 ms     1 ms  172.22.6.1
  3    26 ms    18 ms    20 ms  bs-co-01-pareq2-inet.core.wifirst.net [46.193.247.168]
  4    25 ms    20 ms    22 ms  equinix-paris.core.wifirst.net [195.42.144.142]
  5    21 ms    20 ms    20 ms  equinix-paris.cloudflare.com [195.42.144.143]
  6    22 ms    19 ms    20 ms  172.71.120.4
  7    21 ms    19 ms    22 ms  104.26.11.233

Itinéraire déterminé.


- l'adresse IP publique de la passerelle du réseau (le routeur d'YNOV donc si vous êtes dans les locaux d'YNOV quand vous faites le TP)

```
PS C:\Users\lebou> nslookup myip.opendns.com resolver1.opendns.com
Serveur :   dns.opendns.com
Address:  208.67.222.222

Réponse ne faisant pas autorité :
Nom :    myip.opendns.com
Address:  4195.7.117.146
```



# III. Le requin

- capturez un échange ARP entre votre PC et la passerelle du réseau

En utilisant le filtre 'arp':
[Lien vers capture ARP](./Capture/arp.pcap)

- capturez une requête DNS vers le domaine de votre choix et la réponse

En utiliant le filtre 'dns':
[Lien vers capture DNS](./Capture/dns.pcap)

- vous effectuerez la requête DNS en ligne de commande


- effectuez une connexion qui sollicite le protocole TCP
- je veux voir dans la capture :
  - un 3-way handshake
  - un peu de trafic
  - la fin de la connexion TCP

En uitilisant le filtre 'tcp':
[Lien vers capture TCP](./Capture/tcp.pcap)




