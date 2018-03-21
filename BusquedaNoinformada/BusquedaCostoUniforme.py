from Graph import *
import queue as q


def UniformCostSearch(initial, final, g):

    nodes = g.nodes()
    vertices = {}# pareja de string con el nombre del nodo y una clase nodo que tiene toda la informacion incial que necesito de el
    for n in nodes:
        vertices[n] = Node()

    vertices[initial].setDistance(0)
    node = (0, initial)

    frontier = q.PriorityQueue()
    frontier.put(node)
    explorer = set()

    while not frontier.empty():

        node  = frontier.get() #eliminamos el primer elemento
        if node[1] == final:

            return (True, [vertices,final])

        explorer.add(node[1])
        for nh in g.get(node[1]).keys(): #obtengo las acciones, los nodos mas cercanos desde node

            w = node[0]+ g.get(node[1],nh)

            #validar el recorrido luego de terminado
            if vertices[nh].getDistance() > w:

                vertices[nh].setDistance(w)
                vertices[nh].setConect(node[1])

                child = (w, nh)
                #k = {nh}
                frontier.put(child)
            '''if not k.issubset(explorer) and not vertices[nh].visited:

                frontier.put(child)
            else:'''





    return (False, None)
