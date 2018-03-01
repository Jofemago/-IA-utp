'''IMPLEMENTACION DE LOS METODOS DE BUSQUEDA CON AIMA-PYTHON'''

from aima3.search import Problem
from aima3.search import depth_first_graph_search
from aima3.search import iterative_deepening_search
from Graph import *
from romania import *


class Busqueda(Problem):

    def __init__(self, initial, goal, graph):

        self.initial = initial
        self.goal = goal
        self.g = graph

    def actions(self, state):

        return list(self.g.get(state))

    def result(self, state , action):

        return action


busqueda = Busqueda('Arad', 'Bucharest', romania_map)
depth_first_graph_search(busqueda)
print(iterative_deepening_search(busqueda))

#result = Search.depth_first(GraphProblem('Arad', 'Bucharest', romania_map))
