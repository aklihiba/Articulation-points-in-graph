import graphviz as gv
from collections import defaultdict


class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def degre(self, v):
        return self.graph[v]

    def APUtil(self, u, visited, ap, parent, low, disc):

        children = 0
        visited[u] = True
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1

        for v in self.graph[u]:
            if visited[v] == False:
                parent[v] = u
                children += 1
                self.APUtil(v, visited, ap, parent, low, disc)
                low[u] = min(low[u], low[v])
                if parent[u] == -1 and children > 1:
                    ap[u] = True

                if parent[u] != -1 and low[v] >= disc[u]:
                    ap[u] = True

            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    def AP(self):
        points = list()
        visited = [False] * (self.V)
        disc = [float("Inf")] * (self.V)
        low = [float("Inf")] * (self.V)
        parent = [-1] * (self.V)
        ap = [False] * (self.V)
        i = 0
        for i in range(self.V):
            if visited[i] == False:
                self.APUtil(i, visited, ap, parent, low, disc)
        for index, value in enumerate(ap):
            if value == True:
                points.append(index)
        return points

    def Remove_articualtion_point(self, point):
        del self.graph[point]
        for i in self.graph:
            if point in self.graph[i]:
                self.graph[i].remove(point)

    def PrintGraph(self):
        g = gv.Graph('G', filename="tp3.gv", engine='sfdp')
        for i in self.graph:
            g.edge(str(i), str(self.graph[i]))
        g.view()
        return g


def draw_ap(g, aps):
    g.attr('node', shape='doublecircle')
    for ap in aps:
        g.node(str(ap))
    g.view()
    return


g3 = Graph(7)
g3.addEdge(0, 1)
g3.addEdge(1, 2)
g3.addEdge(2, 0)
g3.addEdge(1, 3)
g3.addEdge(1, 4)
g3.addEdge(1, 6)
g3.addEdge(3, 5)
g3.addEdge(4, 5)
print("initial graph :")
g = g3.PrintGraph()
print()
print("Articulation points in the graph :")

draw_ap(g, g3.AP())

