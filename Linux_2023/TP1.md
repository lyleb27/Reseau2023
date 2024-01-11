# TP1 : Premiers pas Docker
## I. Init
### 3. sudo c pa bo
🌞 Ajouter votre utilisateur au groupe docker
```
[lebou@tp1 ~]$ sudo usermod -aG docker $(whoami)
```
### 4. Un premier conteneur en vif
🌞 Lancer un conteneur NGINX
```
[lebou@tp1 ~]$ docker run -d -p 9999:80 nginx
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
af107e978371: Pull complete
336ba1f05c3e: Pull complete
8c37d2ff6efa: Pull complete
51d6357098de: Pull complete
782f1ecce57d: Pull complete
5e99d351b073: Pull complete
7b73345df136: Pull complete
Digest: sha256:bd30b8d47b230de52431cc71c5cce149b8d5d4c87c204902acf2504435d4b4c9
Status: Downloaded newer image for nginx:latest
f37177fdefd3fc98976efe726b3e58f6e8e3c7967501dece662a33234b78fbfa
```
🌞 Visitons
```
[lebou@tp1 ~]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED              STATUS              PORTS                                       NAMES
f37177fdefd3   nginx     "/docker-entrypoint.…"   About a minute ago   Up About a minute   0.0.0.0:9999->80/tcp, :::9999->80/tcp       strange_faraday
```
```
[lebou@tp1 ~]$ docker inspect f3
[
    {
        "Id": "f37177fdefd3fc98976efe726b3e58f6e8e3c7967501dece662a33234b78fbfa",
        "Created": "2023-12-21T09:51:56.755011135Z",
        "Path": "/docker-entrypoint.sh",
        "Args": [
            "nginx",
            "-g",
            "daemon off;"
        ],
        ...............
    }
]
```
```
[lebou@tp1 ~]$ sudo firewall-cmd --list-all
  ports: 9999/tcp
```
🌞 On va ajouter un site Web au conteneur NGINX
```
[lebou@tp1 nginx]$ ls
index.html  site_nul.conf
```
```
[lebou@tp1 nginx]$ docker run -d -p 9999:8080 -v /home/lebou/nginx/index.html:/var/www/html/index.html -v /home/lebou/nginx/site_nul.conf:/etc/nginx/conf.d/site_nul.conf nginx
203c8ee9bb85639505ce28a09ec2dea531eaa42ca172341c954c91e4d059a43d
```
🌞 Visitons
```
[lebou@tp1 nginx]$ docker ps
CONTAINER ID   IMAGE     COMMAND                  CREATED         STATUS             PORTS                                               NAMES
203c8ee9bb85   nginx     "/docker-entrypoint.…"   4 minutes ago   Up 4 minutes       80/tcp, 0.0.0.0:9999->8080/tcp, :::9999->8080/tcp   frosty_dijkstra
```
### 5. Un deuxième conteneur en vif
🌞 Lance un conteneur Python, avec un shell
```
[lebou@tp1 ~]$ docker run -it python bash
Unable to find image 'python:latest' locally
latest: Pulling from library/python
bc0734b949dc: Pull complete
b5de22c0f5cd: Pull complete
917ee5330e73: Pull complete
b43bd898d5fb: Pull complete
7fad4bffde24: Pull complete
d685eb68699f: Pull complete
107007f161d0: Pull complete
02b85463d724: Pull complete
Digest: sha256:3733015cdd1bd7d9a0b9fe21a925b608de82131aa4f3d397e465a1fcb545d36f
Status: Downloaded newer image for python:latest
root@82a645c8e836:/#
```
🌞 Installe des libs Python
```
root@82a645c8e836:/# pip install aiohttp
root@82a645c8e836:/# pip install aioconsole
```
```
root@82a645c8e836:/# python
Python 3.12.1 (main, Dec 19 2023, 20:14:15) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import aiohttp
>>> import aioconsole
```
## II. Images
### 1. Images publiques
🌞 Récupérez des images
```
[lebou@tp1 ~]$ docker pull python:3.11
Status: Downloaded newer image for python:3.11
docker.io/library/python:3.11
[lebou@tp1 ~]$ docker pull mysql:5.7
Status: Downloaded newer image for mysql:5.7
docker.io/library/mysql:5.7
[lebou@tp1 ~]$ docker pull wordpress:latest
Status: Downloaded newer image for wordpress:latest
docker.io/library/wordpress:latest
[lebou@tp1 ~]$ docker pull linuxserver/wikijs
Status: Downloaded newer image for linuxserver/wikijs:latest
docker.io/linuxserver/wikijs:latest
```
```
[lebou@tp1 ~]$ docker images
REPOSITORY           TAG       IMAGE ID       CREATED        SIZE
linuxserver/wikijs   latest    869729f6d3c5   5 days ago     441MB
mysql                5.7       5107333e08a8   8 days ago     501MB
python               latest    fc7a60e86bae   13 days ago    1.02GB
wordpress            latest    fd2f5a0c6fba   2 weeks ago    739MB
python               3.11      22140cbb3b0c   2 weeks ago    1.01GB
redis                latest    76506809a39f   2 weeks ago    138MB
nginx                latest    d453dd892d93   8 weeks ago    187MB
hello-world          latest    d2c94e258dcb   7 months ago   13.3kB
```
🌞 Lancez un conteneur à partir de l'image Python
```
[lebou@tp1 ~]$ docker run -it 2214 bash
root@34e8eb7698b9:/# python --version
Python 3.11.7
```
### 2. Construire une image
🌞 Ecrire un Dockerfile pour une image qui héberge une application Python
```
[lebou@tp1 python_app_build]$ docker images
REPOSITORY           TAG              IMAGE ID       CREATED        SIZE
python_app           version_de_ouf   f0ea4c8eda33   21 hours ago   638MB
```
🌞 Lancer l'image
```
[lebou@tp1 ~]$ docker run python_app:version_de_ouf
Cet exemple d'application est vraiment naze 👎
```

## III. Docker compose
🌞 Créez un fichier docker-compose.yml
```
[lebou@tp1 ~]$ mkdir /home/lebou/compose_test
[lebou@tp1 ~]$ cd /home/lebou/compose_test/
[lebou@tp1 compose_test]$ nano docker-compose.yml
```
🌞 Lancez les deux conteneurs avec docker compose
```
[lebou@tp1 compose_test]$ docker compose up -d
[+] Running 3/3
 ✔ conteneur_flopesque 1 layers [⣿]      0B/0B      Pulled             3.1s
   ✔ bc0734b949dc Already exists                                       0.0s
 ✔ conteneur_nul Pulled                                                3.5s
[+] Running 3/3
 ✔ Network compose_test_default                  Created               0.3s
 ✔ Container compose_test-conteneur_flopesque-1  Started               0.1s
 ✔ Container compose_test-conteneur_nul-1        Started               0.1s
```
🌞 Vérifier que les deux conteneurs tournent
```
[lebou@tp1 compose_test]$ docker compose top
compose_test-conteneur_flopesque-1
UID    PID    PPID   C    STIME   TTY   TIME       CMD
root   1783   1752   0    09:21   ?     00:00:00   sleep 9999

compose_test-conteneur_nul-1
UID    PID    PPID   C    STIME   TTY   TIME       CMD
root   1768   1729   0    09:21   ?     00:00:00   sleep 9999
```
🌞 Pop un shell dans le conteneur conteneur_nul
```
root@d7a153c64a59:/# apt update
...
root@d7a153c64a59:/# apt install iputils-ping
...
root@d7a153c64a59:/# ping conteneur_flopesque
PING conteneur_flopesque (172.18.0.3) 56(84) bytes of data.
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.3): icmp_seq=1 ttl=64 time=0.062 ms
64 bytes from compose_test-conteneur_flopesque-1.compose_test_default (172.18.0.3): icmp_seq=2 ttl=64 time=0.126 ms
```