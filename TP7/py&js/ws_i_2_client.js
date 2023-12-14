const WebSocket = require('ws');

const socket = new WebSocket('ws://localhost:8765');

socket.on('open', () => {
    console.log('WebSocket connection opened');

    process.stdin.on('data', (data) => {
        const message = data.toString().trim();

        socket.send(JSON.stringify({ message }));
    });
});

socket.on('message', (data) => {
    const message = JSON.parse(data);
    console.log(`Received message from server: ${message.message}`);
});

socket.on('close', () => {
    console.log('WebSocket connection closed');
});

console.log('Enter a string and press Enter to send to the server. Press Ctrl+C to exit.');
