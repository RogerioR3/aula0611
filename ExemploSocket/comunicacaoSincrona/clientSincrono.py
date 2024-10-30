import socket #Importa a biblioteca socket para usar recursos de comunicação em rede.

def send_message(message):
    # Cria um socket TCP/IP (AF_INET indica o protocolo IPv4, SOCK_STREAM indica o protocolo TCP).
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conecta o socket ao servidor que está escutando no 'localhost' na porta 12345.
    client_socket.connect(('localhost', 12345))
    
    # Envia a mensagem codificada em UTF-8 para o servidor.
    client_socket.send(message.encode('utf-8'))
    
    # Recebe a resposta do servidor, decodifica de UTF-8 para string e armazena na variável 'response'.
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {response}")
    
    # Fecha o socket após enviar a mensagem e receber a resposta.
    client_socket.close()

if __name__ == "__main__":
    # Solicita ao usuário uma mensagem a ser enviada ao servidor.
    message = input("Digite a mensagem a ser enviada: ")
    
    # Chama a função 'send_message' passando a mensagem do usuário como argumento.
    send_message(message)


