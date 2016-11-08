#################################################################################
#									SERVER										#
#################################################################################

import socket
import select

####### CONFIG #######
host = ''
port = 333
queue = 5
packetSize = 1024
timeout = 0.05

####### INITIALIZATION #######
pynet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pynet.bind((host, port))
pynet.listen(queue)

print("Server is up on port : {}".format(port))

serverUp = True
connectedClients = []

####### MAIN LOOP #######

while serverUp:
    clients, wlist, xlist = select.select([pynet], [], [], timeout)

    for client in clients:
        clientSocket, clientInfo = client.accept()
        connectedClients.append(clientSocket)

    clientsToRead = []
    try:
        clientsToRead, wlist, xlist = select.select(connectedClients,[], [], timeout)
    except select.error:
        pass
    else:
        for client in clientsToRead:
            message = client.recv(packetSize)
            message = message.decode()
            print("Message = {}".format(message))
            print("Debug = {}".format(message))
            client.send(b"Successfully received\n")
            if message[] == "END":
                serverUp = False

####### SERVER SHUTDOWN #######

print("Server is shutting down")
for client in connectedClients:
    client.close()

pynet.close()
