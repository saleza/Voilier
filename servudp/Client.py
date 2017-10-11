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


lat3 = (float)(trameretour[5] << 24)
lat2 = lat3 + (trameretour[6] << 16)
lat1 = lat2 + (trameretour[7] << 8)
lat0 = lat1 + (trameretour[8])
lat = lat0 / 1000000

longi3 = (float)(trameretour[9] << 24)
longi2 = longi3 + (trameretour[10] << 16)
longi1 = longi2 + (trameretour[11] << 8)
longi0 = longi1 + (trameretour[12])
longi = longi0 / 1000000

print "-------Message renvoye------"
print "ID :", trameretour[0]
print "Longueur du datagram :", trameretour[1]
print "Vitesse du vent :", trameretour[2]
print "Direction du vent :", trameretour[3]
print "Gite :", trameretour[4]
print "Longitude : ", lat
print "Latitude : ", longi
