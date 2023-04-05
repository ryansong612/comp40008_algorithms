from utils.graph_examples import *


def start_bfs(graph, node):
    print("Breadth-first search started...")
    graph.bfs(node)
    print("Breadth-first search finished!")


def start_dfs(graph, node):
    print("Depth-first search started...")
    graph.dfs(node)
    print("Depth-first search finished!")


if __name__ == "__main__":
    start_bfs(graph_1.duplicate(), 1)
    print("")
    start_dfs(graph_1.duplicate(), 1)
