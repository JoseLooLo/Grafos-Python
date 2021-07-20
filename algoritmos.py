from graph import Graph
from collections import deque

def euleriano(g):
    pass


def bbs(filename, vertex_v):
        g = Graph(filename)
        #Da de fazer isso com dict que deve ficar mais rápido
        c = [False for n in range (g.getNumberOfVertices()+1)]
        d = [-1 for n in range (g.getNumberOfVertices()+1)]
        a = [None for n in range (g.getNumberOfVertices()+1)]

        c[vertex_v] = True
        d[vertex_v] = 0

        queue = deque()
        queue.append(vertex_v)
        while len(queue):
            u = queue.popleft()
            for i in g.vList[u].getNeighbors():
                if not c[i]:
                    c[i] = True
                    d[i] = d[u] + 1
                    a[i] = u
                    queue.append(i)

        for i in range(0, max(d)):
            a = str(i)+":"
            for j in range(len(d)):
                if (d[j] == i):
                    a += " "+str(j)
            print(a)