from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)
        self.graph = []

    def addEdge(self,u,v):
        self.edges[u].append(v)
        self.edges[v].append(u)
        self.graph.append([u,v])
    
    def printEdge(self):
        for i in self.edges:
            print(i,end=" => ")
            for j in self.edges[i]:
                print(j,end=" ")
            print()
    
    def dfs_util(self,source,visited):
        visited[source] = 1
        for i in self.edges[source]:
            if visited[i] == 0:
                self.dfs_util(i,visited)

    
def binaryPalindrome(n,k):
    visited = [0]*k # substring of length k
    arr = [0]*n
    g = Graph(k) 
    for i in range(n):
        arr[i] = i%k
    for i in range(n//2):
        g.addEdge(arr[i],arr[n-i-1])
        # g.addEdge(i%k, (n-i-1)%k)

    g.printEdge()
    g.dfs_util(0,visited)
    for i in range(n):
        print(visited[i%k],end = " ")

if __name__ == "__main__":
    binaryPalindrome(24,7)

      