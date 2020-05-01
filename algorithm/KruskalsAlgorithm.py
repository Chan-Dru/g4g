from collections import defaultdict
class Node:
    def __init__(self, parent, rank):
        self.parent = parent
        self.rank = rank

class UnionFind(Node):
    def __init__(self,v):
        self.subsets = []
        self.makeSet(v)

    def makeSet(self,v):
        for i in range(v):
            self.subsets.append(Node(i,0))

    def findSet(self,i):
        if i != self.subsets[i].parent:
            self.subsets[i].parent = self.findSet(self.subsets[i].parent)
        return self.subsets[i].parent
    
    def unionSet(self,iSet,jSet):
        if self.subsets[iSet].rank < self.subsets[jSet].rank:
            self.subsets[iSet].parent = jSet
        elif self.subsets[jSet].rank < self.subsets[iSet].rank:
            self.subsets[jSet].parent = iSet
        else:
            self.subsets[jSet].parent = iSet
            self.subsets[iSet].rank += 1
    
    def isSameSet(self,i,j):
        return self.findSet(i) == self.findSet(j)


class Graph(UnionFind):
    def __init__(self,v):
        self.count = v
        self.graph = []
        self.edges = defaultdict(list)

    def addEdge(self,u,v,w):
        self.edges[u].append([v,w])
        self.graph.append([u,v,w])

    def printEdges(self):
        print("Print edges in graph")
        for source in self.edges:
            print(source,end=" => ")
            for target in self.edges[source]:
                print("{}({})".format(target[0],target[1]),end=" ")
            print()

    def kruskalsAlgorithm(self):
        edges_weight_sorted = sorted(self.graph, key = lambda x: x[2])
        # print(edges_weight_sorted)
        
        edge_count = 0
        uf = UnionFind(self.count)
        g = Graph(self.count)
        for edge in edges_weight_sorted:
            sourceVertex, targetVertex, weight = edge            
            sourceSet = uf.findSet(sourceVertex)
            targetSet = uf.findSet(targetVertex)
            # print(sourceSet,targetSet)
            if sourceSet != targetSet:
                uf.unionSet(sourceSet,targetSet)
                g.addEdge(sourceVertex, targetVertex, weight)
                edge_count += 1
                if edge_count == self.count-1:
                    break
        g.printEdges()
        print("Print Minimum Spanning Tree is",g.graph)



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
    graph.kruskalsAlgorithm()