from graph import Graph
from algoritmos import bbs, euleriano
#https://wiki.python.org/moin/TimeComplexity


#bbs("karate.net", 1)
a = Graph("ex/ContemCicloEuleriano.net")
#euleriano(a)
#a.euleriano()
#print(a.getNumberOfVertices())
#print(a.getNumberOfEdges())
#print(a.getNeighbors(8))
#print(a.getNeighbors(135))
#print(a.hasEdge(1,135))
#print(a.getWeight(1,134))
#a.printBBS(1)
a.floydWarshall()
a.showFloydWarshall()