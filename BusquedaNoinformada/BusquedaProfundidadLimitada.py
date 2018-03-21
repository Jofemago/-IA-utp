from Graph import *


class NodeBPL:

    def __init__(self):


        self.distance = 0
        self.conectividad = None
        self.profundidad = -1



    def setDistance(self, d):

        self.distance = d

    def setConect(self, v):

        self.conectividad = v


    def getConectividad(self):

        return self.conectividad

    def getDistance(self):

        return self.distance

    def setProfundidad(self, d):

        self.profundidad = d


    def getProfu(self):

        return self.profundidad


#algoritmo para la busqueda con profundidad limitada
def BPL(initial, final, g, profundidad):

    nodes = g.nodes()
    vertices = {}# pareja de string con el nombre del nodo y una clase nodo que tiene toda la informacion incial que necesito de el
    for n in nodes:
        vertices[n] = NodeBPL()


    #nivel = 0
    vertices[initial].setProfundidad(0)#este me indica ser la raiz pq no tiene profundidad

    cola = []#FIFO
    cola.append(initial)

    while(len(cola) > 0 ):

        parent = cola.pop(0)
        #nivel +=  1 #

        if parent == final :

            return (True,[vertices,parent])

        #print(vertices[parent].getProfu())
        if vertices[parent].getProfu() < profundidad:

            for nhijo in g.get(parent).keys():
                if vertices[nhijo].getProfu() == -1:#garantizo que no esten explorados
                    vertices[nhijo].setDistance(vertices[parent].getDistance() + g.get(parent, nhijo))
                    vertices[nhijo].setConect(parent)
                    vertices[nhijo].setProfundidad(vertices[parent].getProfu() + 1)
                    #print('padre: ',parent," ", nhijo, vertices[nhijo].getProfu() + 1)
                    cola.append(nhijo)


    return (False,None)
