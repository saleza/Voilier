import socket

class VoilierClient:

    def __init__(self):                             

        self.ipserv = ""
        self.port = 0
        self.safran = 0
        self.GV = 0
        self.gite = 0
        self.latitude = 0 
        self.longitude = 0 
        self.VitVent = 0
        self.OrientVent = 0

    def initCom(self, ip, port):                    

        self.ipserv = ip
        self.port = port
        
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def trx(self):
        
        self.trame = bytearray([1,4,5, 25])
        self.sock.sendto(self.trame, (self.ipserv, self.port))
        self.data, server = self.sock.recvfrom(13)
        self.trameretour = bytearray(self.data)

        lat3 = float(self.trameretour[5] << 24)
        lat2 = lat3 + (self.trameretour[6] << 16)
        lat1 = lat2 + (self.trameretour[7] << 8)
        lat0 = lat1 + (self.trameretour[8])
        
        self.latitude = lat0 / 1000000


        longi3 = (self.trameretour[9] << 24)
        longi2 = longi3 + (self.trameretour[10] << 16)
        longi1 = longi2 + (self.trameretour[11] << 8)
        longi0 = longi1 + (self.trameretour[12])
        longi = longi0

        if self.trameretour[9] > 127:
            longi = (~longi) & 0xFFFFFFFF
            longi = (longi+1) * -1

        self.longitude = longi * 0.000001
     
        print "-------Message renvoye------"
        print "ID :", self.trameretour[0]
        print "Longueur du datagram :", self.trameretour[1]
        print "Vitesse du vent :", self.trameretour[2]
        print "Direction du vent :", self.trameretour[3]
        print "Gite :", self.trameretour[4]
        print "Latitude :", self.latitude
        print "Longitude :", self.longitude

   
testvoilier = VoilierClient()
testvoilier.initCom("127.0.0.1",6423)
testvoilier.trx()
