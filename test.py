from socket import *
serverName = '119.59.99.166'
serverPort = 25000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('input lowercase sentence:')
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()
