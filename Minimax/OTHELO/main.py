from ficha import Ficha
from casilla import Casilla
from othelo import Othelo


def Getjugada():

    x = input('escoja la fila: ')
    y = input('escoja la columna: ')

    #print(x,y)
    return (int(x), int(y))

if __name__=="__main__":

    ot = Othelo()
    #ot.prueba()
    #print(ot)
    #print(ot.getAdjacentes(Casilla(5,5)))

    while(not ot.gameOver()):
        print(ot)
        ot.mostrarTurno()
        ot.MostrarPosiblesMovimientos()
        jugada = Getjugada()
        ot.makeJugada(jugada)
    print(ot)
    #calcular quien gano
