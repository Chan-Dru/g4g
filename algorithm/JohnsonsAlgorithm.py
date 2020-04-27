from collections import defaultdict
import sys
import math

# FibonacciHeap
class FibonacciTree:
    def __init__(self,key,weight):
        self.key = key
        self.weight = weight
        self.parent = None
        self.children = []
        self.order = 0
    
    def add_at_end(self,v):
        v.parent = self
        self.children.append(v)
        self.order += 1

class FibonacciHeap(FibonacciTree):
    def __init__(self):
        self.trees = []
        self.count = 0
        self.least = None
    
    def insert(self,key,weight):
        node = FibonacciTree(key,weight)
        self.trees.append(node)
        self.count += 1
        if self.least is None or  node.weight < self.least.weight:
            self.least = node

    def extractMin(self):
        if self.least is not None:
            node = self.least
            self.trees.remove(node)
            for child in node.children:
                child.parent = None
                self.trees.append(child) 
            self.least = None
            self.count -= 1
            self.consolidate()
            return node          

    def floor_log(self,x):
        return math.frexp(x)[1] - 1

    def consolidate(self):
        count = self.floor_log(self.count)+1
        aux = [None]*count
        while(self.trees != []):
            x = self.trees.pop(0)
            order = x.order
            while(aux[order] is not None):
                y = aux[order]
                if x.weight > y.weight:
                    x,y = y,x
                x.add_at_end(y)
                aux[order]=None
                order += 1
            aux[order] = x

        self.least = None
        for tree in aux:    
            if tree is not None:
                self.trees.append(tree)
                if self.least is None or tree.weight < self.least.weight:
                    self.least = tree

    def isEmpty(self):
        return self.trees == []

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)
        self.graph = []

    def addEdge(self,u,v,w):
        self.edges[u].append([v,w])
        # self.edges[v].append([u,w])
        self.graph.append([u,v,w])
        # self.graph.append([v,u,w])
    
    def printGraph(self):
        for vertex in self.edges:
            print("{} => ".format(vertex), end ="")
            for edge in self.edges[vertex]:
                print("{} ({})".format(edge[0],edge[1]),end ="")
            print()

    def dijkstraAlgorithm(self,sourcevertex):
        maxsize = sys.maxsize
        visited = [False]*self.count
        dist = [maxsize]*self.count
        parent = [None]*self.count
        dist[sourcevertex] = 0
        pq = FibonacciHeap()
        pq.insert(sourcevertex,0)
        while(not pq.isEmpty()):
            # print(pq.trees)
            node = pq.extractMin()
            sourcevertex = node.key
            sourceweigth = node.weight
            # print(sourcevertex,sourceweigth)
            if not visited[sourcevertex]:
                visited[sourcevertex] = True
                for vnode in self.edges.get(sourcevertex,[]):
                    vertex = vnode[0]
                    weight = vnode[1]
                    if not visited[vertex] and sourceweigth + weight < dist[vertex]:
                        newWeight = weight + sourceweigth
                        # print(vertex,newWeight)
                        dist[vertex] = newWeight
                        pq.insert(vertex,newWeight)
                        parent[vertex] = sourcevertex
        # print(dist,parent)
        return dist
        

    def bellmanFordAlgorithm(self,sourceVertex):
        maxsize = sys.maxsize
        dist = [maxsize]*self.count
        parent = [None]*self.count
        dist[sourceVertex] = 0
        for sourceVertex in range(self.count-1):
            for edge in self.graph:
                sourceVertex = edge[0]
                vertex = edge[1]
                weight = edge[2]
                if dist[sourceVertex] != maxsize and weight + dist[sourceVertex] < dist[vertex]:
                    dist[vertex] = weight + dist[sourceVertex]
                    parent[vertex] = sourceVertex
        
        for edge in self.graph:
                sourceVertex = edge[0]
                vertex = edge[1]
                weight = edge[2]
                if dist[sourceVertex] != maxsize and weight + dist[sourceVertex] < dist[vertex]:
                    print("Negative Cycle Found")
                    return

        # print(dist,parent)
        return dist

    def johnsonsAlgorithm(self):
        # initialize a other graph with a new vertex with edges to other vertex
        g = Graph(self.count+1)
        g.graph = self.graph
        g.edges = self.edges
        [g.addEdge(self.count,i,0) for i in range(self.count)]

        # find the shortest dist from the new vertex using BellmanFord Algorithm
        sourceVertex = self.count
        dist = g.bellmanFordAlgorithm(sourceVertex)

        # remove the newly added vertex and reform the graph with modified weight - no negarive weight
        g.edges = defaultdict(list)
        g.graph = []
        g.count -= 1
        for edge in self.edges:
            u = edge
            for v,w in self.edges[u]:
                w = w + dist[u] - dist[v]
                g.addEdge(u,v,w)

        # run dijkstrasAlgorithm for all vetex
        for sourceVertex in range(g.count):
            dist = g.dijkstraAlgorithm(sourceVertex)
            print("Shortest path from vertex {} to others is {}".format(sourceVertex,dist))
        

if __name__ == "__main__":
    graph = Graph(4)
    graph.addEdge(0,1,-5)
    graph.addEdge(0,2,2)
    graph.addEdge(0,3,3)
    graph.addEdge(1,2,4)
    graph.addEdge(2,3,1)
    sourceVertex = 0
    graph.johnsonsAlgorithm()