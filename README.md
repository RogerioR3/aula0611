# Sistemas Distribuídos

Este repositório contém exemplos e implementações relacionadas ao curso de **Sistemas Distribuídos**, incluindo um sistema de troca de mensagens (chat) utilizando Socket.IO e exemplos de comunicação síncrona e assíncrona.

## Estrutura do Repositório

### 1. AplicacaoChat

A pasta `AplicacaoChat` contém o código para um sistema de troca de mensagens em tempo real, desenvolvido com Flask e Socket.IO. Este projeto permite a comunicação em grupo e entre usuários em um ambiente distribuído, proporcionando uma interface de chat que suporta:

- Troca de mensagens em tempo real.
- Mensagens privadas entre usuários.
- Notificações de entrada e saída dos usuários no chat.

#### Principais Tecnologias Usadas
- **Flask**: Framework web para o backend.
- **Socket.IO**: Biblioteca para comunicação em tempo real entre cliente e servidor.

### 2. ExemploSocket

A pasta `ExemploSocket` contém exemplos de comunicação síncrona e assíncrona, implementados para fins educacionais e testes. Esses exemplos demonstram diferentes abordagens para comunicação em rede em ambientes distribuídos, ilustrando o funcionamento e as diferenças entre os dois tipos de comunicação.

#### Principais Funcionalidades
- **Comunicação Síncrona**: Exemplo de como enviar e receber mensagens de forma bloqueante, onde a execução aguarda uma resposta para continuar.
- **Comunicação Assíncrona**: Exemplo de como enviar e receber mensagens sem bloqueio, permitindo que o sistema processe outras tarefas enquanto aguarda uma resposta.

## Como Executar

### Pré-requisitos

- **Python 3.x**
- **Docker** (opcional, para executar o RabbitMQ com facilidade)
- **Bibliotecas Python**: Instale as dependências com o comando abaixo
  ```bash
  pip install -r requirements.txt 
  ```

### Contribuições

- Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para sugerir melhorias ou corrigir problemas.