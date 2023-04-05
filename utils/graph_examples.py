from utils.arc import Arc
from utils.graph import Graph


# Remember duplicating graph before use

# Example 1
nodes_1 = [x for x in range(9)]
arcs_1 = [Arc(1, 2), Arc(2, 3), Arc(2, 4), Arc(4, 5), Arc(1, 8),
          Arc(4, 8), Arc(4, 6), Arc(6, 7), Arc(7, 8)]
graph_1 = Graph(nodes_1, arcs_1)
