from graph import Graph
from collections import deque

def euleriano(g):
    c = {}
    for i in range(1,g.getNumberOfVertices()+1):
        for j in g.vList[i].getNeighbors():
            a = (i,j)
            c[a] = False

    r, ciclo = subEuleriano(g, valid(g), c)
    if r:
        print("1")
        print(ciclo)
    else:
        print("0")

def subEuleriano(g, vertex_v, c):
    ciclo = []
    ciclo.append(vertex_v)
    t = vertex_v
    while True:
        for i in g.vList[t].getNeighbors():
            a = (i,t)
            b = (t,i)
            if not c[a]:
                c[a] = True
                c[b] = True
                t = i
                ciclo.append(t)
                break
        else:
            return False,None
        if vertex_v == t:
            break

    for i in ciclo:
        for j in g.vList[i].getNeighbors():
            a = (i,j)
            if not c[a]:
                r, ciclo2 = subEuleriano(g, i, c)
                if not r:
                    return False, None
                index = ciclo.index(i)
                del ciclo[index]
                for i in range(len(ciclo2)):
                    ciclo.insert(index+i, ciclo2[i])

    return True, ciclo

def valid(g):
    for i in range(1,g.getNumberOfVertices()+1):
        if len(g.vList[i].getNeighbors()) > 0:
            return i



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