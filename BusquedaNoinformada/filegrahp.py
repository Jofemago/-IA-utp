

from Graph import *
from romania import *
from BusquedaCostoUniforme import *
from BusquedaProfundidadLimitada import *
from BusqProfundidadIter import *




#Busqueda Costo Uniforme
#res = UniformCostSearch('Arad', 'Bucharest', romania_map)


#Busqueda con profundidad limitada
#res = BPL('Sibiu', 'Neamt', romania_map,0)

#Busqueda con profundiad iterativa
res = BPIter('Sibiu', 'Neamt', romania_map)
l = []
if res[0]:
    j = res[1][0][res[1][1]]
    l.append(res[1][1])
    while j.getConectividad() != 'Sibiu':
        l.append(j.getConectividad())
        j = res[1][0][j.getConectividad()]

    l.append(j.getConectividad())
else:
    print('estado no alcanzable o profundidad muy pequena')
print(l)
#print(res[1][0][res[1][1]].getDistance())


#print(romania_map.get('Arad','Sibiu'))
#DFS3(romania_map,'Arad' )
#BFS(romania_map,'Arad' , 'Bucharest')
#print(romania_map.get('Arad').keys())
#print(romania_map.dict['Arad'].keys())
#print(romania_map.get('Urziceni').keys())
