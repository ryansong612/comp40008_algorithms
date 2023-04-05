class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = nodes
        self.arcs = arcs
        self.visited = {node: False for node in self.nodes}
        self.parent = {node: None for node in self.nodes}

    def adj(self, x):
        adjacent_nodes = []
        for arc in self.arcs:
            if arc.start == x:
                adjacent_nodes.append(arc.end)
            if arc.end == x:
                adjacent_nodes.append(arc.start)
        return sorted(adjacent_nodes)

    def dfs(self, x):
        self.visited[x] = True
        print(f"We go to {x}")
        for y in self.adj(x):
            if not self.visited[y]:
                self.parent[y] = x
                self.dfs(y)
        # backtrack to x
        if self.parent[x]:
            print(f"We backtrack to {self.parent[x]}")

    def bfs(self, x):
        q = []
        self.visited[x] = True
        print(f"We go to {x}")
        q.append(x)
        while len(q) != 0:
            y = q[0]
            for z in self.adj(y):
                if not self.visited[z]:
                    self.visited[z] = True
                    print(f"We go to {z} from {y}")
                    self.parent[z] = y
                    q.append(z)
            q.pop(0)

    def cycleDFS(self, x):
        self.visited[x] = True
        print(x)
        for y in self.adj(x):
            if self.visited[y] and y != self.parent[x]:
                # cycle found involving x and y
                return x, y
            if not self.visited[y]:
                self.parent[y] = x
                pair = self.cycleDFS(y)
                if pair:
                    return pair
        return None

    def duplicate(self):
        return Graph(self.nodes, self.arcs)

