from utils.graph_examples import *


def start_bfs(graph, node):
    print("Breadth-first search started...")
    graph.duplicate().bfs(node)
    print("Breadth-first search finished!")


def start_dfs(graph, node):
    print("Depth-first search started...")
    graph.duplicate().dfs(node)
    print("Depth-first search finished!")


def detect_cycles_dfs(graph, node):
    print("Detecting whether cycles are present...")
    pair = graph.duplicate().cycleDFS(node)
    if pair:
        result = "there is a cycle present!"
    else:
        result = "no cycle found!"
    print(f"Detection complete: {result}")


def run_topological_sort(graph):
    print("Topologically sorting...")
    new_graph = graph.duplicate()
    result = new_graph.topological_sort()
    print(result)
    print("Topological sort complete")


if __name__ == "__main__":
    start_bfs(graph_1, 1)
    print("")
    start_dfs(graph_1, 1)
    print("")
    detect_cycles_dfs(graph_2, 1)
    print("")
    detect_cycles_dfs(graph_4, 1)
    print("")
    run_topological_sort(graph_1_19)

