from ficha import Ficha

class Casilla:

    def __init__(self, posX, posY , ficha = None ):

        self.ficha_ = ficha
        self.posX_ = posX
        self.posY_ = posY


    def __str__(self):
        
        strr = str(self.posX_) + '_' +str(self.posY_)
        return strr


    def setFicha(self, turno):

        self.ficha_ = Ficha(turno)

    def esOcupada(self):

        return self.ficha_ is not None

    def rotarFicha(self):

        if(self.esOcupada()):

            self.ficha_.rotarFicha()
