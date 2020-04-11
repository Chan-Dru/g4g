import copy
from collections import defaultdict

class Graph():
    def __init__(self,v):
        self.length = v
        self.edges = defaultdict(list)
    
    def printGraph(self):
        print(self.edges)

    def addEdge(self,u,v,w=1):
        self.edges[u].append(v)

    def DFS_util(self,start,end,visited,level):
        visited[start] = level
        if start==end:
            print("path order",visited)
        else:
            for i in self.edges[start]:
                if visited[i] == -1:
                    self.DFS_util(i,end,visited,level+1)
        visited[start] = -1

    # Backtracking to find the path from u to v
    def countPath(self,start,end):
        visited = [-1]*self.length
        self.DFS_util(start,end,visited,0)
        

if __name__ == "__main__":
    g = Graph(4);
    # g.printGraph() 
    g.addEdge(0,0)
    g.addEdge(1,1)
    g.addEdge(2,2)
    g.addEdge(3,3)
    g.addEdge(0, 1); 
    g.addEdge(0, 2); 
    g.addEdge(0, 3); 
    g.addEdge(2, 0); 
    g.addEdge(2, 1); 
    g.addEdge(1, 3); 
    g.printGraph()
    g.countPath(2,3)
