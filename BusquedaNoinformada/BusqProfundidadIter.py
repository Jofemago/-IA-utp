from Graph import *
from BusquedaProfundidadLimitada import *

def BPIter(initial, final, g, it = 50):
    '''Se manejara haran maximo 50 iteraciones, obviamente puede elejir las iteraciones que desee '''

    for i in range(it):
        print('iteracion: ', i)
        res = BPL(initial,final,g, i)
        if(res[0]):
            return res
