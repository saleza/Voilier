import socket

UDP_IP = "192.168.0.234"
UDP_PORT = 6423

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

print "Serveur Actif"

while True:
    data, addr = sock.recvfrom(1024)
    print "Received message :", data
