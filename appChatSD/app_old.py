from flask import Flask, render_template
from flask_socketio import SocketIO, send
from flask_cors import CORS  # Importa o CORS

# Inicializa o Flask (um framework web em Python)
app = Flask(__name__)

# Habilita CORS (Cross-Origin Resource Sharing) no Flask, permitindo que o backend seja acessado por diferentes origens
CORS(app)

# Configura uma chave secreta para o Flask, usada internamente para segurança (como em sessões)
app.config['SECRET_KEY'] = 'mysecret'

# Inicializa o SocketIO com o Flask, permitindo comunicação em tempo real via WebSockets
# O parâmetro 'cors_allowed_origins="*"' permite conexões de qualquer origem (CORS para WebSockets)
socketio = SocketIO(app, cors_allowed_origins="*")

# Define a rota principal da aplicação. Quando o usuário acessa o endereço '/', a função 'index' é chamada
@app.route('/')
def index():
    # Renderiza o template HTML chamado 'index.html', que deve estar na pasta 'templates'
    return render_template('index.html')

# Evento que trata mensagens enviadas pelos clientes via WebSocket
@socketio.on('message')
def handleMessage(msg):
    # Imprime a mensagem recebida no console do servidor
    print('Mensagem recebida: ' + msg)
    
    # Envia a mensagem recebida de volta para todos os clientes conectados (broadcast=True)
    send(msg, broadcast=True)

# Inicia o servidor Flask-SocketIO
if __name__ == '__main__':
    # Faz o servidor Flask-SocketIO rodar a aplicação
    socketio.run(app)
