import pika
from flask import Flask, render_template
from flask_socketio import SocketIO
import threading
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app, cors_allowed_origins="*")

# Configura SocketIO para um nível de log mínimo
socketio = SocketIO(app, cors_allowed_origins="*", logger=False, engineio_logger=False)

# Desabilitar logs de nível INFO e DEBUG
logging.getLogger('werkzeug').setLevel(logging.WARNING)  # Desativa logs do Flask (Werkzeug)
logging.getLogger('socketio').setLevel(logging.WARNING)   # Desativa logs do Socket.IO
logging.getLogger('engineio').setLevel(logging.WARNING)   # Desativa logs do Engine.IO

# Função para enviar a mensagem para o RabbitMQ
def send_to_rabbitmq(message):
    connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0'))
    channel = connection.channel()
    channel.queue_declare(queue='chatQueue')
    channel.basic_publish(exchange='', routing_key='chatQueue', body=message)
    connection.close()

# Função para consumir mensagens do RabbitMQ e distribuí-las aos clientes via WebSocket
def consume_from_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('0.0.0.0'))
    channel = connection.channel()
    channel.queue_declare(queue='chatQueue')

    def callback(ch, method, properties, body):
        message = body.decode()
        socketio.emit('message', message)  # Emite mensagem para todos os clientes conectados
        socketio.emit('log', f"Mensagem do servidor: {message}")  # Envia log para os clientes

    channel.basic_consume(queue='chatQueue', on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(f'Mensagem recebida do cliente: {msg}')
    send_to_rabbitmq(msg)  # Envia a mensagem para o RabbitMQ
    socketio.emit('log', f"Mensagem recebida do cliente: {msg}")  # Envia log para os clientes

if __name__ == '__main__':
    # Inicia o consumo do RabbitMQ em uma thread separada
    threading.Thread(target=consume_from_rabbitmq).start()
    socketio.run(app, host='0.0.0.0', port=5000, debug=False)
