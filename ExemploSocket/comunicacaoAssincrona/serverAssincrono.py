import socket  # Importa a biblioteca de sockets, essencial para comunicação em rede.
import threading  # Importa a biblioteca de threads, necessária para lidar com múltiplas conexões simultâneas.

# Lista global para armazenar todos os sockets dos clientes conectados
clients = []

# Função que lida com a comunicação de um cliente
def handle_client(client_socket, addr):
    try:
        # Recebe o nome do cliente logo após a conexão
        name = client_socket.recv(1024).decode('utf-8')
        print(f"{name} ({addr}) entrou na sala.")  # Imprime o nome e endereço do cliente que se conectou.
        broadcast(f"{name} entrou na sala.", client_socket)  # Informa a todos os clientes que um novo cliente entrou na sala.

        while True:
            # Recebe a mensagem do cliente
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break  # Sai do loop se não houver mensagem.
            print(f"{name}: {message}")  # Imprime a mensagem recebida juntamente com o nome do cliente.
            broadcast(f"{name}: {message}", client_socket)  # Envia a mensagem para todos os outros clientes.
    except:
        pass
    finally:
        # Remove o cliente da lista de clientes conectados e fecha o socket em caso de erro ou desconexão
        clients.remove(client_socket)
        client_socket.close()
        print(f"{name} ({addr}) saiu da sala.")  # Imprime uma mensagem indicando que o cliente saiu da sala.
        broadcast(f"{name} saiu da sala.", client_socket)  # Informa a todos os clientes que um cliente saiu da sala.

# Função que envia a mensagem recebida para todos os clientes, exceto o remetente
def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:  # Garante que a mensagem não será enviada de volta ao remetente.
            try:
                client.send(message.encode('utf-8'))  # Envia a mensagem ao cliente.
            except:
                clients.remove(client)  # Remove o cliente da lista se houver erro ao enviar a mensagem.
                client.close()  # Fecha o socket do cliente.

# Função principal que inicia o servidor
def start_server():
    server_ip = '0.0.0.0'  # O servidor aceitará conexões em todas as interfaces de rede.
    server_port = 12345
    
    # Cria um objeto socket usando IPv4 e TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Associa o socket ao endereço IP e porta especificados
    server_socket.bind((server_ip, server_port))
    
    # Coloca o servidor em modo de escuta com um limite de 5 conexões pendentes
    server_socket.listen(5)
    print(f"Servidor esperando por conexões em {server_ip}:{server_port}...")

    while True:
        # Aceita uma conexão do cliente
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)  # Adiciona o socket do cliente à lista de clientes.
        
        # Cria e inicia uma nova thread para lidar com o cliente
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()
        
        # Imprime o número de conexões ativas
        print(f"Conexões ativas: {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()  # Chama a função para iniciar o servidor.