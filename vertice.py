class Vertice:
    def __init__(self, label):
        self.label = label
        self.degree = 0
        self.eList = {}
        self.v = []

    def insertEdge(self, vertex_q, weight):
        self.eList[vertex_q] = weight
        self.v.append(vertex_q)
        self.degree += 1

    def getNeighbors(self):
        return self.v

    def getDegree(self):
        return self.degree

    def getLabel(self):
        return self.label