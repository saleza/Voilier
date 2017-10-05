import socket
from TrameCli import Trame

UDP_IP = "127.0.0.1"
UDP_PORT = 6423

trame1 = Trame()
tabtrame = trame1.tableauTrame()

trame = bytearray(tabtrame)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
sock.sendto(trame, (UDP_IP, UDP_PORT))

data, server = sock.recvfrom(13)
trameretour = bytearray(data)
print "-------Message renvoye------"
print "ID :", trameretour[0]
print "Longueur du datagram :", trameretour[1]
print "Vitesse du vent :", trameretour[2]
print "Direction du vent :", trameretour[3]
print "Gite :", trameretour[4]
