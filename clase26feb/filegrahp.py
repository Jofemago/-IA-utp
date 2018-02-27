
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
'''recibe nodo inicial para grafos totalmente conexos, si no estan todos los nodos conectados
    puee que queden nodos sin recorrer'''
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




def UndiretedGraph(dict = None):

    return Graph(dict = dict, directed = False)



romania_map = UndiretedGraph(dict(
    Arad = dict(Zerind = 75, Sibiu = 140, Timisoara = 118),
    Bucharest = dict(Urziceni = 85, Pitesti = 101, Giurgiu = 90, Fagaras = 211),
    Craiova = dict(Drobeta = 120, Rimnicu = 146, Pitesti = 138),
    Drobeta = dict(Mehadia = 75),
    Eforie =  dict(Hisora = 86),
    Fagaras = dict(Sibiu = 99),
    Hisora = dict(Urziceni = 98),
    Iasi = dict(Vaslui = 92, Neamt = 87),
    Lugoj = dict(Timisoara = 111, Mehadia = 70),
    Oradea  = dict(Zerind = 71, Sibiu = 151),
    Pitesti = dict(Rimnicu= 97),
    Rimnicu = dict(Sibiu = 80),
    Urziceni = dict(Vaslui = 142)


))



DFS3(romania_map,'Arad' )
#print(romania_map.get('Urziceni').keys())
