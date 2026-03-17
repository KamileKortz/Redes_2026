import socket

HOST = "0.0.0.0"
PORT = 9008

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    
    #Conecta o servidor
    s.connect((HOST, PORT))
    
    #Recebe mensagem do servidor
    msg = s.recv(1024).decode()
    print(msg)

    msg = s.recv(1024).decode()
    print(msg)