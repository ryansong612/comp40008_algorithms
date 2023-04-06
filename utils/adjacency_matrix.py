from utils.arc import Arc
from utils.graph import Graph


class AdjacencyMatrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def toGraph(self):
        # number of nodes
        dim = len(self.matrix)
        nodes = [n for n in range(1, dim + 1)]
        arcs = []

        for i in range(dim):
            for j in range(dim):
                if self.matrix[i][j] != 0:
                    # arc or loop present
                    arcs.append(Arc(i + 1, j + 1))
        return Graph(nodes, arcs)
