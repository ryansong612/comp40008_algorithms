from utils.adjacency_matrix import AdjacencyMatrix
from utils.arc import Arc
from utils.graph import Graph

# Remember duplicating graph before use

# Example 1
nodes_1 = [x for x in range(1, 9)]
arcs_1 = [Arc(1, 2), Arc(2, 3), Arc(2, 4), Arc(4, 5), Arc(1, 8),
          Arc(4, 8), Arc(4, 6), Arc(6, 7), Arc(7, 8)]
graph_1 = Graph(nodes_1, arcs_1)

# Example 2
nodes_2 = [x for x in range(1, 4)]
arcs_2 = [Arc(i, i + 1) for i in range(1, 3)]
graph_2 = Graph(nodes_2, arcs_2)

# Example 3
nodes_3 = [x for x in range(1, 3)]
arcs_3 = [Arc(1, 2), Arc(2, 1)]
graph_3 = Graph(nodes_3, arcs_3)

# Example 4
matrix_4 = AdjacencyMatrix([[0, 1, 0, 1, 0],
                            [1, 0, 1, 0, 1],
                            [0, 1, 0, 1, 0],
                            [1, 0, 1, 0, 1],
                            [0, 1, 0, 1, 0]])
graph_4 = matrix_4.toGraph()


# Figure 1.19
nodes_1_19 = [x for x in range(1, 8)]
arcs_1_19 = [Arc(1, 2), Arc(6, 2), Arc(2, 7),
             Arc(2, 5), Arc(3, 4), Arc(4, 5)]
graph_1_19 = Graph(nodes_1_19, arcs_1_19)

# Figure 1.22
matrix_1_22 = AdjacencyMatrix([[0, 1, 1, 1],
                               [1, 0, 1, 0],
                               [1, 1, 0, 1],
                               [1, 0, 1, 0]])
weights_1_22 = [[0, 3, 5, 4],
                [3, 0, 4, 0],
                [5, 4, 0, 2],
                [4, 0, 2, 0]]
graph_1_22 = matrix_1_22.toGraph()
graph_1_22.set_weights(weights_1_22)

