from vertice import Vertice
from collections import deque

class Graph:
    def __init__(self, filename):
        self.nVertices = 0
        self.nEdges = 0
        self.vList = {}
        self.readFile(filename)

    def readFile(self, filename):
        with open(filename) as f:
            content = f.readlines()
            self.nVertices = int(content[0].split()[1])
            for i in range(1, self.nVertices+1):
                vertex = content[i].split()
                self.insertVertex(int(vertex[0]), " ".join(vertex[1:]))
            for i in range(self.nVertices+2, len(content)):
                edge = content[i].split()
                self.insertEdge(int(edge[0]), int(edge[1]), float(edge[2]))
                self.nEdges += 1

    def insertVertex(self, vertex, label):
        v = Vertice(label)
        self.vList[vertex] = v

    def insertEdge(self, vertex_v, vertex_q, weight):
        self.vList[vertex_v].insertEdge(vertex_q, weight)
        self.vList[vertex_q].insertEdge(vertex_v, weight)

    def getNumberOfVertices(self):
        return self.nVertices

    def getNumberOfEdges(self):
        return self.nEdges

    def getLabel(self, i):
        return self.vList[i].getLabel()

    def getDegree(self, vertex_v):
        return self.vList[vertex_v].getDegree()

    def getNeighbors(self, vertex_v):
        return self.vList[vertex_v].getNeighbors()

    def hasEdge(self, vertex_v, vertex_q):
        return vertex_q in self.vList[vertex_v].eList

    def getWeight(self, vertex_v, vertex_q):
        if self.hasEdge(vertex_v, vertex_q):
            return self.vList[vertex_v].eList[vertex_q]
        return float('inf')

    def euleriano(self):
        c = {}
        for i in range(1,self.getNumberOfVertices()+1):
            for j in self.vList[i].getNeighbors():
                a = (i,j)
                c[a] = False

        r, ciclo = self.subEuleriano(3, c)
        if r:
            print("1")
            print(ciclo)
        else:
            print("0")

    def subEuleriano(self, vertex_v, c):
        ciclo = []
        ciclo.append(vertex_v)
        t = vertex_v
        while True:
            for i in self.vList[t].getNeighbors():
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
            for j in self.vList[i].getNeighbors():
                a = (i,j)
                if not c[a]:
                    r, ciclo2 = self.subEuleriano(i, c)
                    if not r:
                        return False, None
                    index = ciclo.index(i)
                    del ciclo[index]
                    for i in range(len(ciclo2)):
                        ciclo.insert(index+i, ciclo2[i])

        return True, ciclo

    def bbs(self, vertex_v):
        #Da de fazer isso com dict que deve ficar mais rápido
        c = [False for n in range (self.getNumberOfVertices()+1)]
        d = [-1 for n in range (self.getNumberOfVertices()+1)]
        a = [None for n in range (self.getNumberOfVertices()+1)]

        c[vertex_v] = True
        d[vertex_v] = 0

        queue = deque()
        queue.append(vertex_v)
        while len(queue):
            u = queue.popleft()
            for i in self.vList[u].getNeighbors():
                if not c[i]:
                    c[i] = True
                    d[i] = d[u] + 1
                    a[i] = u
                    queue.append(i)

        return d,a

    def printBBS(self, vertex_v):
        d,a = self.bbs(vertex_v)
        for i in range(0, max(d)):
            a = str(i)+":"
            for j in range(len(d)):
                if (d[j] == i):
                    a += " "+str(j)
            print(a)