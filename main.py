#!/usr/bin/python
# -*- coding: utf-8 -*-

from graph import Graph
from algoritmos import bbs, euleriano
#https://wiki.python.org/moin/TimeComplexity


a = Graph("ex/agm_tiny.net")

# Atividade 1

#bbs("karate.net", 1)
#euleriano(a)
#a.euleriano()
#print(a.getNumberOfVertices())
#print(a.getNumberOfEdges())
#print(a.getNeighbors(8))
#print(a.getNeighbors(135))
#print(a.hasEdge(1,135))
#print(a.getWeight(1,134))
#a.printBBS(1)
#a.floydWarshall()
#a.showFloydWarshall()
#d, ant = a.dijkstra(6)
#a.showDijkstra(d, ant)

# Atividade 2

#a.showSCC()
#a.ordenacaoTopologica()
a.kruskal()