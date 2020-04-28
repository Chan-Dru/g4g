from collections import defaultdict
import sys

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)

    def addEdges(self,u,v,w):
        self.edges[u].append([v,w])
    
    # Bellman Ford Algorithm
    def isThereNegtiveCycle(self):
        maxsize = sys.maxsize
        dist = [maxsize]*self.count

        # Calculate shortest distance from source vertex
        dist[0] = 0 #sourceVertex
        for _ in range(self.count-1):
            for sourceVertex in self.edges:
                for edge in self.edges[sourceVertex]:
                    vertex, weight = edge
                    if dist[sourceVertex] != maxsize and dist[sourceVertex] + weight < dist[vertex]:
                        dist[vertex] = dist[sourceVertex] + weight
        
        # print(dist)
        # Check is there a negative cycle
        for sourceVertex in self.edges:
            for edge in self.edges[sourceVertex]:
                    vertex, weight = edge
                    if dist[sourceVertex] != maxsize and dist[sourceVertex] + weight < dist[vertex]:
                        return True

        return False

if __name__ == "__main__":
    # g = Graph(5)
    # g.addEdges(0,1,-1)
    # g.addEdges(0,2,4)
    # g.addEdges(1,2,3)
    # g.addEdges(1,3,2)
    # g.addEdges(1,4,2)
    # g.addEdges(3,2,5)
    # g.addEdges(3,1,1)
    # g.addEdges(4,3,-3)
    g = Graph(4)
    g.addEdges(0,1,1)
    g.addEdges(1,2,-1)
    g.addEdges(2,3,-1)
    g.addEdges(3,0,-1)

    result = g.isThereNegtiveCycle()
    output = "Negative Cycle is found" if result else "Negative Cycle is not found"   
    print(output)


