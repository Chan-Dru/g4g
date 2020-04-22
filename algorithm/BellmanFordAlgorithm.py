# Detect negative cycle and report the shortest path from source vertex to all vertex in graph

import sys
from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.graph =[]
        self.length = v
        self.edges = defaultdict(list)

    def printEdges(self):
        for vertex in self.edges:
            print(vertex,"=>",self.edges[vertex])

    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
        self.edges[u].append([v,w])

    def shortestPath(self,sourceVertex):
        maxSize = sys.maxsize
        dist = [maxSize]*self.length
        dist[sourceVertex] = 0
        for vertex in range(self.length-1): # vertex except sourceVertex
            for edge in self.graph: # for all edges in graph
                u,v,w = edge
                if dist[u] != maxSize and dist[u] + w < dist[v]: # update the dist with shortest path
                    dist[v] = dist[u] + w

        for edge in self.graph:
            u,v,w = edge
            if dist[u] != maxSize and dist[u] + w < dist[v]:
                print("Negative Cycle is Found, shortest path can't be found")
                return

        print("Shortest path from source vertex {} to other vertex is {}".format(sourceVertex,dist))

if __name__ == "__main__":
    g = Graph(5) 
    g.addEdge(0, 1, -1) 
    g.addEdge(0, 2, 4) 
    g.addEdge(1, 2, 3) 
    g.addEdge(1, 3, 2) 
    g.addEdge(1, 4, 2) 
    g.addEdge(3, 2, 5) 
    g.addEdge(3, 1, 1) 
    g.addEdge(4, 3, -3) 
    
    # Print the solution 
    g.shortestPath(0) 