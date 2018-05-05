

class Ficha:

    def __init__(self, color):

        self.color_ = color
        #color va ser una variable que es -1 o 1, -1 blanco, 1 negro


    def rotarFicha(self):

        self.color_ = self.color_ * -1
