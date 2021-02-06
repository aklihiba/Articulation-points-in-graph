from collections import defaultdict
import graphviz as gv
import networkx as nx
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.graph = defaultdict(list)
        self.Time = 0

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        self.graph[v].append(u)

    def degre(self, v):
        return self.graph[v]

    def APUtil(self,u, visited, ap, parent, low, disc): 
  
        children =0
        visited[u]= True
        disc[u] = self.Time 
        low[u] = self.Time 
        self.Time += 1
  
        for v in self.graph[u]: 
            if visited[v] == False : 
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
        for i in range(self.V ): 
            if visited[i] == False: 
                self.APUtil(i, visited, ap, parent, low, disc) 
        for index, value in enumerate (ap): 
            if value == True: points.append(index)
        return points

    def Remove_articualtion_point(self, point):
        del self.graph[point]
        for i in self.graph: 
            if point in self.graph[i] : self.graph[i].remove(point)
 
    def PrintGraph(self):
        for i in self.graph : print(i,self.graph[i])
    
    def DrawGraph(self):
        G = nx.Graph()
        for i in self.graph:
            G.add_node(i)
        for i in self.graph:  
            for j in self.graph[i]:
                G.add_edge(j, i)
            
        
        nx.draw(G, with_labels=True, font_weight='bold')
        plt.figure(100)
        #plt.show()
        #plt.cla()
        #plt.cla()
    
    def Color(self):
        G = nx.Graph()
        for i in self.graph:
            G.add_node(i)
        for i in self.graph:  
            for j in self.graph[i]:
                G.add_edge(j, i)
        
        pos = nx.spring_layout(G, seed=3113794652)  # positions for all nodes
        # nodes
        options = {"edgecolors": "tab:gray", "node_size": 800, "alpha": 0.9}
        nx.draw_networkx_nodes(G, pos, nodelist=list(G.nodes), node_color="tab:blue", **options)
        nx.draw_networkx_nodes(G, pos, nodelist=self.AP(), node_color="tab:red", **options)
        nx.draw_networkx_edges(G, pos, width=1.0, alpha=0.5)
    
        nx.draw_networkx_edges(
            G,
            pos,
            edgelist=list(G.edges),
            width=3,
            alpha=0.5,
            edge_color="tab:blue",
        )


        plt.tight_layout()
        plt.axis("off")
        plt.figure(200)
        #plt.cla()
       


g3 = Graph (7) 
g3.addEdge(0, 1) 
g3.addEdge(1, 2) 
g3.addEdge(2, 0) 
g3.addEdge(1, 3) 
g3.addEdge(1, 4) 
g3.addEdge(1, 6) 
g3.addEdge(3, 5) 
g3.addEdge(4, 5) 


"""
g3.PrintGraph()
g3.DrawGraph()
g3.Color()
"""
print ("Articulation points in third graph ")
print(g3.AP()) 
