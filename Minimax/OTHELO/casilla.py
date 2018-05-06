from ficha import Ficha

class Casilla:

    def __init__(self, posX, posY , ficha = None ):

        self.ficha_ = ficha
        self.posX_ = posX
        self.posY_ = posY


    def __str__(self):

        #strr = str(self.posX_) + '_' +str(self.posY_)
        strr = " "
        if self.esOcupada():
            strr = str(self.ficha_)

        return strr

    def getFicha(self):

        return self.ficha_


    def setFicha(self, turno):

        self.ficha_ = Ficha(turno)

    def esOcupada(self):

        return self.ficha_ is not None

    def rotarFicha(self):

        if(self.esOcupada()):

            self.ficha_.rotarFicha()

    def getPos(self):

        return (self.posX_ , self.posY_)
