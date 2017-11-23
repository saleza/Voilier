import socket

class VoilierClient:

    def __init__(self):                             

        self.ipserv = ""
        self.port = 0
        self.ID = 0
        self.valSF = 0
        self.valGV = 0
        self.gite = 0
        self.latitude = 0 
        self.longitude = 0 
        self.vitVent = 0
        self.orientVent = 0

    def initCom(self, ip, port):                    

        self.ipserv = ip
        self.port = port
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)     

    def txrx(self, valSF, valGV):

        self.valSF = valSF
        self.valGV = valGV
        self.trame = bytearray([self.ID, 2, self.valSF, self.valGV])
        self.sock.sendto(self.trame, (self.ipserv, self.port))
        self.data, server = self.sock.recvfrom(30)
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

        self.gite=self.trameretour[4]
        self.vitVent=self.trameretour[2]
        self.orientVent=self.trameretour[3]
     
        print "-------Message renvoye------"
        print "ID :", self.trameretour[0]
        print "Longueur du datagram :", self.trameretour[1]
        print "Vitesse du vent :", self.trameretour[2]
        print "Direction du vent :", self.trameretour[3]
        print "Gite :", self.trameretour[4]
        print "Latitude :", self.latitude
        print "Longitude :", self.longitude

