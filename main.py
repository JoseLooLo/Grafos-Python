from graph import Graph
from algoritmos import bbs
#https://wiki.python.org/moin/TimeComplexity


#bbs("karate.net", 1)
a = Graph("ContemCicloEuleriano.net")
a.euleriano()
#print(a.getNumberOfVertices())
#print(a.getNumberOfEdges())
#print(a.getNeighbors(8))
#print(a.getNeighbors(135))
#print(a.hasEdge(1,135))
#print(a.getWeight(1,134))
a.printBBS(1)