import socket  # Importa a biblioteca de sockets, essencial para comunicação em rede.
import threading  # Importa a biblioteca de threads, necessária para lidar com recepção e envio de mensagens simultaneamente.

# Função que recebe mensagens do servidor
def receive_messages(client_socket):
    while True:
        try:
            # Recebe a mensagem do servidor
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  # Sai do loop se não houver mensagem.
            print(f"{message}")  # Imprime a mensagem recebida.
        except:
            print("Erro ao receber mensagem")  # Imprime uma mensagem de erro.
            client_socket.close()  # Fecha o socket do cliente.
            break  # Sai do loop.

# Função que envia mensagens ao servidor
def send_message(client_socket):
    while True:
        message = input()  # Lê a mensagem digitada pelo usuário.
        client_socket.send(message.encode('utf-8'))  # Envia a mensagem ao servidor.

if __name__ == "__main__":
    server_ip = '0.0.0.0'  # Endereço IP do servidor.
    server_port = 12345
    
    # Cria um objeto socket usando IPv4 e TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conecta o socket do cliente ao servidor
    client_socket.connect((server_ip, server_port))
    
    # Solicita o nome do usuário e envia para o servidor
    name = input("Digite seu nome: ")
    client_socket.send(name.encode('utf-8'))  # Envia o nome do cliente ao servidor.

    # Cria e inicia uma thread para receber mensagens
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # Cria e inicia uma thread para enviar mensagens
    send_thread = threading.Thread(target=send_message, args=(client_socket,))
    send_thread.start()