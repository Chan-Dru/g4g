# Minimum Spanning Tree
from collections import defaultdict
import sys
import math

class FibonacciTree:
    def __init__(self,key,weight):
        self.key = key
        self.weight = weight
        self.children = []
        self.parent = None
        self.order = 0

    def add_at_end(self,node):
        node.parent = self
        self.children.append(node)
        self.order += 1

class PriorityQueue(FibonacciTree):
    def __init__(self):
        self.heap = []
        self.least = None
        self.count = 0
    
    def insert(self,key,weight):
        node = FibonacciTree(key,weight)
        self.heap.append(node)
        self.count += 1
        if self.least is None or node.weight < self.least.weight:
            self.least = node

    def extractMin(self):
        node = self.least
        self.heap.remove(node)
        for child in node.children:
            child.parent = None
            self.heap.append(child)
        self.count -= 1
        self.consolidate()
        return node
    
    def floor2log(self,count):
        return math.frexp(count)[1] - 1

    def consolidate(self):
        l = self.floor2log(self.count) + 1
        aux = [None]*l
        while(self.heap != []):
            x = self.heap.pop(0)
            order = x.order
            while(aux[order] is not None):
                y = aux[order]
                if x.weight > y.weight:
                    x,y = y,x
                x.add_at_end(y)
                aux[order] = None
                order += 1
            aux[order] = x
        
        self.least = None
        for node in aux:
            if node is not None:
                self.heap.append(node)
                if self.least is None or node.weight < self.least.weight:
                    self.least = node


class Graph(PriorityQueue):
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)
    
    def addEdge(self,u,v,w):
        self.edges[u].append([v,w])
        self.edges[v].append([u,w])

    def primsAlgorithm(self):
        maxsize = sys.maxsize
        visited = [False]*self.count
        dist = [maxsize]*self.count
        parent = [None]*self.count
        pq = PriorityQueue()
        dist[0] = 0
        pq.insert(0,0)

        while(pq.heap != []):
            node = pq.extractMin()
            source = node.key
            visited[source] = True
            sourceWeight = node.weight
            for child in self.edges.get(source,[]):
                target = child[0]
                targetWeight = child[1]
                # newWeight = sourceWeight + targetWeight
                if not visited[target] and targetWeight < dist[target]:
                    dist[target] = targetWeight
                    parent[target] = source
                    pq.insert(target,targetWeight)
        
        print("MST: Parent of each vertex {}".format(parent))


if __name__ == "__main__":
    graph = Graph(9) 
    graph.addEdge(0, 1, 4) 
    graph.addEdge(0, 7, 8) 
    graph.addEdge(1, 2, 8) 
    graph.addEdge(1, 7, 11) 
    graph.addEdge(2, 3, 7) 
    graph.addEdge(2, 8, 2) 
    graph.addEdge(2, 5, 4) 
    graph.addEdge(3, 4, 9) 
    graph.addEdge(3, 5, 14) 
    graph.addEdge(4, 5, 10) 
    graph.addEdge(5, 6, 2) 
    graph.addEdge(6, 7, 1) 
    graph.addEdge(6, 8, 6) 
    graph.addEdge(7, 8, 7)
    graph.primsAlgorithm()