import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 6423
Id = 5
Taille = 8
VitVent = 30
DirVent = 6
Gite = 4
latitude = 48.3389
longitude = -17.04575

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

latsansvirgule = int(latitude*1000000)
lat3 = (latsansvirgule >> 24)&0xFF
lat2 = (latsansvirgule >> 16)&0xFF
lat1 = (latsansvirgule >> 8)&0xFF
lat0 = (latsansvirgule)&0xFF

longisansvirgule = int(longitude*1000000)
longi3 = (longisansvirgule >> 24)&0xFF
longi2 = (longisansvirgule >> 16)&0xFF
longi1 = (longisansvirgule >> 8)&0xFF
longi0 = (longisansvirgule)&0xFF

print "Serveur Actif"

while True:
    trame, addr = sock.recvfrom(4)
    data = bytearray(trame)
    trameretour = bytearray([Id,Taille,VitVent,DirVent,Gite,lat3,lat2,lat1,lat0,longi3,longi2,longi1,longi0])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(trameretour, (addr[0], addr[1]))
    print '---------Message recu---------'
    print "ID :", data[0]
    print "Taille :", data[1]
    print "Safran :", data[2]
    print "GV :", data[3]