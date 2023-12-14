const WebSocket = require('ws');

const socket = new WebSocket('ws://localhost:8765');

socket.on('open', () => {
    console.log('WebSocket connection opened');

    process.stdin.on('data', (data) => {
        const message = data.toString().trim();

        socket.send(message);
    });
});

socket.on('message', (data) => {
    const message = data.toString();
    console.log(`Message reçu du serveur : ${message}`);
});

socket.on('close', () => {
    console.log('WebSocket connection closed');
});

console.log('Entrez un message et appuyez sur Entrée pour l\'envoyer au serveur. Appuyez sur Ctrl+C pour quitter.');
