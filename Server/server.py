#################################################################################
#									SERVER										#
#################################################################################

import socket
import configparser

####### READ THE CONFIG FILE #######
config = configparser.ConfigParser()
config.read('./server.conf')
port = int(config['server']['Port'])
queue = int(config['server']['Queue size'])

####### INIT THE SERVER #######
pynet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pynet.bind(('', port))
print("Server started on port {}".format(port))

pynet.listen(queue)

client, client_infos = pynet.accept()
print("New connection = {0}:{1}".format(client_infos[0],client_infos[1]))
client.send(b"Connection accepted")
