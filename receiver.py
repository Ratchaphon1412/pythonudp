from socket import *

serverPort = 25000

serverSocket = socket(AF_INET, SOCK_DGRAM)

serverSocket.bind(('0.0.0.0', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
    print("Message received from client: ", message.decode())
