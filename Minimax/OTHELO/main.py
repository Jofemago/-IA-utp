from ficha import Ficha
from casilla import Casilla
from othelo import Othelo

def Getjugada(l):

    x = input('escoja la fila: ')
    y = input('escoja la columna: ')
    if (x<0 or x > 7 or y<0 or y>7) or ((x,y) not in l):
        print ('jugada no valida intente de nuevo')
        Getjugada(l)
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
        l = ot.RetornarPosiblesMovimientos()
        jugada = Getjugada(l)
        ot.makeJugada(jugada)

    print(ot)
    ot.CalcularGanador()
    #calcular quien gano
