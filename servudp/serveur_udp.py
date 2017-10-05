import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 6423

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print "Serveur Actif"

while True:
    trame, addr = sock.recvfrom(4)
    data = bytearray(trame)
    trameretour = bytearray([5,4,8,6,4])
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(trameretour, (addr[0], addr[1]))
    print '---------Message recu---------'
    print "ID :", data[0]
    print "Longueur du datagram :", data[1]
    print "Safran :", data[2]
    print "GV :", data[3]
