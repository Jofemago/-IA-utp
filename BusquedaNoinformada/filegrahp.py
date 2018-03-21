

from Graph import *
from romania import *
from BusquedaCostoUniforme import *

#Busqueda Costo Uniforme
res = UniformCostSearch('Arad', 'Bucharest', romania_map)
l = []
if res[0]:
    j = res[1][0][res[1][1]]
    l.append(res[1][1])
    while j.getConectividad() != 'Arad':
        l.append(j.getConectividad())
        j = res[1][0][j.getConectividad()]

    l.append(j.getConectividad())
print(l)
print(res[1][0][res[1][1]].getDistance())
#print(romania_map.get('Arad','Sibiu'))
#DFS3(romania_map,'Arad' )
#BFS(romania_map,'Arad' , 'Bucharest')
#print(romania_map.get('Arad').keys())
#print(romania_map.dict['Arad'].keys())
#print(romania_map.get('Urziceni').keys())
