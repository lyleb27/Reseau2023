import argparse

def main():
    parser = argparse.ArgumentParser(description="Simple server with port configuration.")
    parser.add_argument("-p", "--port", type=int, help="Port number to listen on. Must be between 0 and 65535.")
    args = parser.parse_args()

    if args.port is not None:
        if args.port < 0 or args.port > 65535:
            print("ERROR: Le port spécifié n'est pas un port possible (de 0 à 65535).")
            exit(1)
        if args.port <= 1024:
            print("ERROR: Le port spécifié est un port privilégié. Spécifiez un port au-dessus de 1024.")
            exit(2)

    if args.port is None:
        args.port = 13337

    print(f"Serveur en cours d'exécution sur le port {args.port}")

if __name__ == "__main__":
    main()
