class Trame:

    def __init__(self):

        self.ID=0
        self.Taille=2
        self.Safran=4
        self.GV=5

    def tableauTrame(self): 

        tableauTrame = [self.ID , self.Taille , self.Safran , self.GV]
        return tableauTrame

test = Trame()
test.tableauTrame()




