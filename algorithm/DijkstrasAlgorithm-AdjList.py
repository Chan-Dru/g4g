from collections import defaultdict
import sys
import heapq

# Priority Queue
class MinHeap():
    def __init__(self):
        self.arr = []

    def insert(self,a):
        self.arr.append(a)
        self.heapify()

    def minHeap(self,i,n):
        smallest = i
        l = 2*i +1
        r = 2*i +2
        if l<n and self.arr[l][1] < self.arr[smallest][1]:
            smallest = l
        if r<n and self.arr[r][1] < self.arr[smallest][1]:
            smallest = r
        if i != smallest:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
    
    def decreaseKey(self,i,v):
        self.arr[i][1] = v
        parent = (i-1)//2
        while(parent >= 0 and self.arr[i][1] < self.arr[parent][1]):
            self.arr[parent], self.arr[i] = self.arr[i], self.arr[parent]
            i = parent
            parent = (i-1)//2

    def extractMin(self):
        t = self.arr.pop(0)
        self.heapify()
        return t
    
    def heapify(self):
        n = len(self.arr)
        for i in range(n//2+1,-1,-1):
            self.minHeap(i,n)

    def isEmpty(self):
        return len(self.arr) == 0


class Node():
    def __init__(self,v,w):
        self.key = v
        self.weight = w
        self.next = None

class Graph(MinHeap,Node):
    def __init__(self,v):
        self.length = v
        self.edges = defaultdict()

    def addEdge(self,u,v,w):
        if self.edges.get(u) == None:
            self.edges[u] = Node(v,w)
        else:
            n = self.edges[u]
            while(n.next != None):
                n = n.next
            n.next = Node(v,w)

        if self.edges.get(v) == None:
            self.edges[v] = Node(u,w)
        else:
            n = self.edges[v]
            while(n.next != None):
                n = n.next
            n.next = Node(u,w)

    
    def printGraph(self):
        for row in self.edges:
            print(row, " => ",end ="")
            node = self.edges[row]
            while(node is not None):
                print(" {} ({})".format(node.key,node.weight),end ="")
                node = node.next
            print()


    def shortestPath(self,sourceVertex):
        pq = MinHeap()
        visited = [False]*self.length
        finalWeight = [sys.maxsize]*self.length
        parent = [None]*self.length

        finalWeight[sourceVertex] = 0
        pq.insert([sourceVertex,0]) # sourcevertex and its weight
                
        while(not pq.isEmpty()):
            job = pq.extractMin()
            sourceVertex = job[0]
            weight = job[1]
            # print(sourceVertex,weight)
            if not visited[sourceVertex]:
                visited[sourceVertex] = True
                node = self.edges.get(sourceVertex,None)
                while(node is not None):
                    vertex = node.key
                    value = node.weight
                    if not visited[vertex] and value + weight < finalWeight[vertex]:
                        newWeight = value + weight
                        finalWeight[vertex] = newWeight
                        pq.insert([vertex,newWeight])
                        parent[vertex] = sourceVertex
                    node = node.next

        print("Parent of each vertex {}".format(parent))
        return finalWeight
            

        


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
    sourceVertex = 0
    # graph.printGraph()
    print("Shortest path from vertex {} to others is {}".format(sourceVertex,graph.shortestPath(sourceVertex)))
    # [0, 4, 12, 19, 21, 11, 9, 8, 14]

