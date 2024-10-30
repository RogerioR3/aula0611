var socket = io();

// Exibe uma mensagem de conexão bem-sucedida
socket.on('connect', function() {
    var messages = document.getElementById('messages');
    var newMessage = document.createElement('div');
    newMessage.textContent = '🟢 Conectado ao servidor!';
    messages.appendChild(newMessage);
});

// Exibe uma mensagem de desconexão
socket.on('disconnect', function() {
    var messages = document.getElementById('messages');
    var newMessage = document.createElement('div');
    newMessage.textContent = '🔴 Desconectado do servidor.';
    messages.appendChild(newMessage);
});

// Evento para capturar a mensagem enviada pelo servidor e exibi-la
socket.on('message', function(msg) {
    var messages = document.getElementById('messages');
    var newMessage = document.createElement('div');
    newMessage.textContent = msg;
    messages.appendChild(newMessage);
});

// Função para enviar a mensagem
document.getElementById('send-btn').onclick = function() {
    var input = document.getElementById('message-input');
    var message = input.value;
    socket.send(message);  // Enviar a mensagem para o servidor
    input.value = '';  // Limpar o campo de entrada
};


// Exibe uma mensagem de conexão bem-sucedida
socket.on('connect', function() {
    var messages = document.getElementById('messages');
    var newMessage = document.createElement('div');
    newMessage.className = 'system-message connected';
    newMessage.textContent = '🟢 Conectado ao servidor!';
    messages.appendChild(newMessage);
});

// Exibe uma mensagem de desconexão
socket.on('disconnect', function() {
    var messages = document.getElementById('messages');
    var newMessage = document.createElement('div');
    newMessage.className = 'system-message disconnected';
    newMessage.textContent = '🔴 Desconectado do servidor.';
    messages.appendChild(newMessage);
});
