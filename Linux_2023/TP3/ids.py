import json
import os
import hashlib
import argparse
import logging

LOG_FILE = '/var/ids/ids.log'
DB_FILE = '/var/ids/db.json'

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def build():
    "Construit un fichier JSON qui contient un état des choses à surveiller."
    data = {}

    file_path = '/var/ids/db.json'
    file_hash = hash_file(file_path)
    data[file_path] = file_hash

    # Enregistrement dans le fichier JSON
    with open(DB_FILE, 'w') as json_file:
        json.dump(data, json_file, indent=2)

    logging.info('Commande build exécutée. Fichier JSON créé.')

def check():
    "Vérifie que l'état actuel est conforme à ce qui a été stocké dans le fichier JSON."
    if not os.path.exists(DB_FILE):
        logging.error(f'Le fichier {DB_FILE} n\'existe pas. Exécutez d\'abord la commande "build".')
        return

    with open(DB_FILE, 'r') as json_file:
        expected_state = json.load(json_file)

    current_state = {file_path: hash_file(file_path) for file_path in expected_state.keys()}

    if current_state == expected_state:
        logging.info('{"state": "ok"}')
    else:
        logging.warning('{"state": "divergent", "changes": %s}', json.dumps(find_changes(expected_state, current_state)))

def hash_file(file_path):
    "Retourne le hash d'un fichier."
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_changes(expected_state, current_state):
    "Retourne les changements entre l'état attendu et l'état actuel."
    changes = {}
    for file_path in expected_state.keys():
        if expected_state[file_path] != current_state[file_path]:
            changes[file_path] = {
                'expected_hash': expected_state[file_path],
                'current_hash': current_state[file_path]
            }
    return changes

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="IDS - Intrusion Detection System")
    parser.add_argument("command", choices=["build", "check"], help="Commande à exécuter")
    args = parser.parse_args()

    if args.command == "build":
        build()
    elif args.command == "check":
        check()
