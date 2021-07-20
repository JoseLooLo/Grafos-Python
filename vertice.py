class Vertice:
    def __init__(self, label):
        self.label = label
        self.degree = 0
        self.eList = {}

    def insertEdge(self, vertex_q, weight):
        self.eList[vertex_q] = weight
        self.degree += 1

    def getNeighbors(self):
        #Da de tornar essa lista padrão da classe para diminuir a complexidade para O(1)
        v = []
        for i,k in self.eList.items():
            v.append(i)
        return v

    def getDegree(self):
        return self.degree

    def getLabel(self):
        return self.label