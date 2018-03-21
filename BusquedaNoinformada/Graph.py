
class Graph(object):

    def __init__(self, dict = None, directed = True):

        self.dict = dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    def make_undirected(self):

        for a in list(self.dict.keys()):
                for (b,dist) in self.dict[a].items():
                    self.connect1(b,a,dist)

    def connect(self, A, B, distance = 1):

        self.connect1(A,B, distance)
        if not self.directed:
            self.connect1(B,A,distance)

    def connect1(self, A,B, distance):

        self.dict.setdefault(A, {})[B] = distance

    def get(self, a, b = None):

        links = self.dict.setdefault(a, {})
        if b is None:
            return links

        else:
            return links.get(b)


    def nodes(self):

        return list(self.dict.keys())




#--------------------------------------------------------------------------------


def AllVisit(dict):

    for e in dict.keys():
        if not dict[e]:
            return False
    return True

def GetNextNode(dict):

    for e in dict.keys():
        if not dict[e]:
            return e
    return

def hasUnunvisitedNode(visitados, nodos):

    for l in nodos:
        if not visitados[l]:
            return (l,True)
    return (None,False)

def  DFS( graph):

    stack = []
    nodes = graph.nodes()
    visitados = {}
    for n in nodes:
        visitados[n] = False

    while(not AllVisit(visitados)):

        v = GetNextNode(visitados)
        stack.append(v)

        while len(stack) > 0:
            x = stack[len(stack) - 1]
            links = graph.get(x).keys()
            result = hasUnunvisitedNode(visitados, links)

            if result[1]:

                visitados[result[0]] = True
                stack.append(result[0])

            else:

                stack.pop()

def  DFS3( graph, v):
    '''recibe nodo inicial para grafos totalmente conexos, si no estan todos los nodos conectados puede que queden nodos sin recorrer'''
    stack = []
    nodes = graph.nodes()
    visitados = {}
    for n in nodes:
        visitados[n] = False
    stack.append(v)
    visitados[v] = True #lo marco como visitado
    print(v)#lo muestro para visualizacion
    while len(stack) > 0:
        x = stack[len(stack) - 1]
        links = graph.get(x).keys()
        result = hasUnunvisitedNode(visitados, links)

        if result[1]:

            visitados[result[0]] = True
            print(result[0])
            stack.append(result[0])
        else:

            stack.pop()


    #print(visitados)
#----------------------------------------------------------------------------------------------------
class Node:

    def __init__(self):

        self.Color = 'BLANCO'
        self.distance = float('inf')
        self.conectividad = None

    def setColor(self, color):

        self.Color = color

    def setDistance(self, d):

        self.distance = d

    def setConect(self, v):

        self.conectividad = v


    def GetColor(self):

        return self.Color

    def getConectividad(self):

        return self.conectividad

    def getDistance(self):

        return self.distance



def EcontrarNodosVisitados(vertices, s,d):#O(n)
    '''se encarga de revisar los nodos por lo que tuvo que pasar el algoritmo BFS antes de llegar al destino d'''

    j = d

    print(d)
    while(j != s):

        j = vertices[j].getConectividad()
        print(j)


def BFS(g,v,d):

    nodes = g.nodes()
    vertices = {}# pareja de string con el nombre del nodo y una clase nodo que tiene toda la informacion incial que necesito de el
    for n in nodes:
        vertices[n] = Node()


    vertices[v].setColor('GRIS')
    vertices[v].setDistance(0)
    #ya el nodo tiene conectividad nula

    cola = []
    cola.append(v)
    #print(v)

    while(len(cola) > 0):

        u = cola.pop(0)
        for nh in g.get(u).keys():

            if vertices[nh].GetColor() == 'BLANCO':

                vertices[nh].setColor('GRIS')
                vertices[nh].setDistance(vertices[u].getDistance() + 1)
                vertices[nh].setConect(u)


                if nh == d:
                    #print('se encontro')
                    cola = []
                    EcontrarNodosVisitados(vertices, v, d)
                else:
                    cola.append(nh)

                #print(nh)

        vertices[u].setColor('NEGRO')






def UndiretedGraph(dict = None):

    return Graph(dict = dict, directed = False)
