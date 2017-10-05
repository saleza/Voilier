class Trame:

    def __init__(self):

        self.ID=0
        self.Taille=2
        self.Vitvent=25
        self.Dirven=0
        self.gite=0

    def tableauTrame(self): 

        tableauTrame = [self.ID , self.Taille , self.Vitven , self.Dirvent]
        return tableauTrame

test = Trame()
test.tableauTrame()
