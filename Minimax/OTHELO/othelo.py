from ficha import Ficha
from casilla import Casilla

class Othelo:

    N = 8

    def __init__(self, turno = 1):

        self.tablero_ = [[Casilla(X,Y) for Y in range(0, self.N)] for X in range(0, self.N)]
        self.confInicial()
        self.NroFichas = 4
        #inicializar las 4 fichas
        self.turno_ = 1



    def makeJugada(self, jugada):

        self.tablero_[jugada[0]][jugada[1]].setFicha(self.turno_)
        self.NroFichas += 1
        #self.turno_ = self.turno_ * -1

        k = self.getAdjacentes(self.tablero_[jugada[0]][jugada[1]])
        for pos in k:
            if self.isOcupadaCasilla(pos):
                cas = self.tablero_[pos[0]][pos[1]]
                if cas.getFicha().getColor() != self.turno_ :
                    cas.rotarFicha()

        self.turno_ = self.turno_ * -1

    def MostrarPosiblesMovimientos(self):

        l = []
        for i in range(self.N):
            for j in range(self.N):

                if self.tablero_[i][j].esOcupada():

                    k = self.getAdjacentes(self.tablero_[i][j])
                    for pos in k:
                        if not self.isOcupadaCasilla(pos):
                            #calcular si es valida las pos
                            l.append(pos)
        l = set(l)
        print('los posibles movimientios: ')
        for e in l:
            print(e)

    def calcularValidez(self, pos, x, y):

        i = pos[0]
        j = pos[1]
        itera = (pos[0] + x , pos[1] + y )
        color = False
        while(self.inbordes(itera)):

            if not self.isOcupadaCasilla(itera):
                return False
            if self.tablero_[itera[0]][itera[1]].getFicha().getColor == self.turno_ and not color:
                return False
            elif self.tablero_[itera[0]][itera[1]].getFicha().getColor != self.turno_:
                color = True
                itera = (itera[0] + x , itera[1] + y )
                #continuar


        return True

    def inbordes(self, pos):

        return pos[0] >= 0 and pos[0] <= 7 and pos[1] >= 0 and pos[1] <= 7


    def RetornarPosiblesMovimientos(self):

        l = []
        for i in range(self.N):
            for j in range(self.N):

                if self.tablero_[i][j].esOcupada():

                    k = self.getAdjacentes(self.tablero_[i][j])
                    for pos in k:
                        if not self.isOcupadaCasilla(pos):
                            l.append(pos)
        l = set(l)
        return l

    def isOcupadaCasilla(self, pos):

        return self.tablero_[pos[0]][pos[1]].esOcupada()

    def getAdjacentes(self, casilla):

        l = []
        pos = casilla.getPos()

        l.append(( pos[0] , pos[1] - 1)) #izq
        l.append(( pos[0] , pos[1] + 1)) #der
        l.append(( pos[0] - 1 , pos[1] )) #arr
        l.append(( pos[0] + 1 , pos[1] )) #abj

        l.append(( pos[0] -1   , pos[1] -1 )) #izqarr
        l.append(( pos[0] + 1 , pos[1] - 1)) #izqabj
        l.append(( pos[0] - 1, pos[1] + 1)) #derarr
        l.append(( pos[0] + 1, pos[1] + 1 )) #deraba


        return [e for e in l if e[0] <= 7 and e[0] >= 0 and  e[1] <= 7 and e[1] >= 0  ]



    def mostrarTurno(self):

        if self.turno_ == 1:
            print('juega Negro')
        if self.turno_ == -1:
            print('juega Blanco')

    def confInicial(self):
        '''define la cofiguraacion inicial'''

        turno = -1
        for i in range(3,5):
            for j in range(3,5):

                self.tablero_[i][j].setFicha(turno)
                turno = turno *-1
            turno = turno *-1

    def gameOver(self):

        return self.NroFichas == 64

    def __str__(self):

        strr = '# # # # # # # # ' + '\n'
        for i in range(8):
            for j in range(8):
                strr += str(self.tablero_[i][j]) + ' '
            strr += '\n'

        strr += '# # # # # # # # ' + '\n'
        return strr


    def CalcularGanador(self):

        b = 0
        n = 0
        for i in range(self.N):
            for j in range(self.N):
                if self.tablero_[i][j].ficha_.esNegro():
                    n += 1
                elif self.tablero_[i][j].ficha_.esBlanco():
                    b += 1
        if b > n:
            print ('han ganado las fichas blancas !!!')
        elif n > b:
            print ('han ganado las fichas negras !!!')
        else:
            print('empate !!!')
"""
    def prueba(self):
        strr = ''
        for i in range(8):
            for j in range(8):
                strr += str(self.tablero_[i][j])
            strr += '\n'
        print(strr)"""
