from collections import defaultdict
import copy

class Graph:
    def __init__(self,v):
        self.length = v
        self.graph = []
        self.edge = defaultdict(list)
        for i in range(self.length):
            self.graph.append([0]*self.length)
            self.graph[i][i] = 0
        self.tc = copy.deepcopy(self.graph)
    
    def printGraph(self):
        for i in self.graph:
            print(i)

    def addEdge(self,u,v):
        self.graph[u][v] = 1
        self.edge[u].append(v)
    
    # Using Floyd's Warshall Algorithm
    def transitiveClosure(self):
        transitive_closure = copy.deepcopy(self.graph)
        for k in range(self.length):
            for i in range(self.length):
                for j in range(self.length):
                    transitive_closure[i][j] = transitive_closure[i][j] or (transitive_closure[i][k] and transitive_closure[k][j] )
                    # shortest path finding
                    # value = transitive_closure[i][k] + transitive_closure[k][j]
                    # transitive_closure[i][j] = min(value, transitive_closure[i][j])

        print("Transitivie Closure using Floyd's Warshall Algorithm")
        for i in transitive_closure:
            print(i)
        
    def DFS_util(self,start,end):
        self.tc[start][end] = 1
        for i in self.edge[end]:
            if self.tc[start][i] == 0:
                self.DFS_util(start,i)
                

    def transitiveClosureUsingDFS(self):
        for i in range(self.length):
            self.DFS_util(i,i)

        print("Transitivie Closure Using DFS Method")
        for i in self.tc:
            print(i)



if __name__ == "__main__":
    g = Graph(4) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)

    g.printGraph()
    g.transitiveClosure()
    g.transitiveClosureUsingDFS()