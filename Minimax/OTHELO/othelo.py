from ficha import Ficha
from casilla import Casilla

class Othelo:

    N = 8

    def __init__(self):
        self.Nrofichas = 0
        self.tablero_ = [[Casilla(X,Y) for Y in range(0, self.N)] for X in range(0, self.N)]

        #inicializar las 4 fichas

    def prueba(self):
        strr = ''
        for i in range(8):
            for j in range(8):
                strr += str(self.tablero_[i][j]) + ' '
            strr += '\n'
        print(strr)
