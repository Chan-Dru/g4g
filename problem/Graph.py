from collections import defaultdict
import copy

class Graph():
    
    def __init__(self,v,directed = True):
        self.directed = directed
        self.length = v
        self.edges = defaultdict(list)
        self.graph = [[0 for i in range(v)] for i in range(v)]
        self.tc = copy.deepcopy(self.graph)

    def printGraph(self):
        print("Graph Matrix")
        for i in self.graph:
            print(i)
    
    def printEdges(self):
        print("Graph Edges")
        for i in self.edges:
            print(i,"=>",self.edges[i])
        
    def addEdge(self,u,v,w=1):
        self.edges[u].append(v)
        self.graph[u][v] = w
        if not self.directed:
            self.graph[v][u] = w
            self.edges[v].append(u)

    