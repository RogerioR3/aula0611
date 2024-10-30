import socket

def start_server():
    #Criação do Socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Cria um socket TCP/IP.

    #Associação e Escuta (Servidor)
    server_socket.bind(('localhost', 12345))  #Associa o socket do servidor ao endereço IP local e à porta 12345.
    server_socket.listen(5)                   #Coloca o servidor em modo de escuta para aceitar conexões.
    print("Servidor esperando por conexões...")

    while True:
        #Conexão (Cliente):
        client_socket, addr = server_socket.accept()  #Conecta o socket do cliente ao endereço IP e porta do servidor.
        print(f"Conexão estabelecida com {addr}")

        while True:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Mensagem recebida: {message}")
            client_socket.send("Mensagem recebida".encode('utf-8'))
        
        client_socket.close()
        print(f"Conexão com {addr} encerrada")

if __name__ == "__main__":
    start_server()