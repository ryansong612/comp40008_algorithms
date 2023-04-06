from utils.arc import Arc


class Graph:
    def __init__(self, nodes, arcs):
        self.nodes = nodes
        self.arcs = arcs
        self.weights = []
        self.visited = {node: False for node in self.nodes}
        self.parent = {node: None for node in self.nodes}

        # topological sort
        self.n = len(self.nodes)
        self.ts = [0] * self.n
        self.index = 0
        self.entered = {node: False for node in self.nodes}
        self.exited = {node: False for node in self.nodes}

        # MST algorithms
        self.tree = {node: False for node in self.nodes}

    def set_weights(self, new_weights):
        self.weights = new_weights

    def adj(self, x):
        adjacent_nodes = []
        for arc in self.arcs:
            if arc.start == x:
                adjacent_nodes.append(arc.end)
            if arc.end == x:
                adjacent_nodes.append(arc.start)
        return sorted(adjacent_nodes)

    def directed_adj(self, x):
        adjacent_nodes = []
        for arc in self.arcs:
            if arc.start == x:
                adjacent_nodes.append(arc.end)
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

    def shortest_path(self, x):
        distance = {}
        q = []
        self.visited[x] = True
        distance[x] = 0
        q.append(x)
        while len(q) != 0:
            y = q[0]
            for z in self.adj(y):
                if not self.visited[z]:
                    self.visited[z] = True
                    self.parent[z] = y
                    distance[z] = distance[y] + 1
                    q.append(z)
            q.pop(0)
        return self.parent

    def topological_sort(self):
        self.index = self.n - 1
        for node in self.nodes:
            if not self.entered[node]:
                self.dfs_topological_sort(node)
        return self.ts

    def dfs_topological_sort(self, x):
        self.entered[x] = True
        for y in self.directed_adj(x):
            if self.entered[y]:
                if not self.exited[y]:
                    print("Cycle Found")
                    return
            else:
                self.parent[y] = x
                self.dfs_topological_sort(y)
        self.exited[x] = True
        self.ts[self.index] = x
        self.index -= 1
        return

    def weigh(self, x, y):
        return self.weights[x - 1][y - 1]

    def empty_fringe(self, fringe):
        for f in fringe:
            if fringe[f]:
                return False
        return True

    def prim_MST_classic(self, start):
        fringe = {node: False for node in self.nodes}
        weight = {node: 99999 for node in range(len(self.nodes) + 1)}
        mst = []

        self.tree[start] = True
        for x in self.adj(start):
            fringe[x] = True
            self.parent[x] = start
            weight[x] = self.weigh(start, x)

        while not self.empty_fringe(fringe):
            min_f = 0
            for f in fringe:
                if fringe[f]:
                    if weight[f] < weight[min_f]:
                        min_f = f
            fringe[min_f] = False
            self.tree[min_f] = True
            mst.append(Arc(self.parent[min_f], min_f))
            for y in self.adj(min_f):
                if not self.tree[y]:
                    if fringe[y]:
                        # update candidate arc
                        if self.weigh(min_f, y) < weight[y]:
                            weight[y] = self.weigh(min_f, y)
                            self.parent[y] = min_f
                    else:
                        # y is unseen
                        fringe[y] = True
                        weight[y] = self.weigh(min_f, y)
                        self.parent[y] = min_f
        return mst

    def duplicate(self):
        if self.weights:
            dup = Graph(self.nodes, self.arcs)
            dup.set_weights(self.weights)
            return dup
        else:
            return Graph(self.nodes, self.arcs)
