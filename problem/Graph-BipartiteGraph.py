from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.graph = []
        self.edges = defaultdict(list)
    
    def addEdge(self,u,v,w=0):
        self.edges[u].append(v)
        self.edges[v].append(u)

    def printEdge(self):
        print("Print edges in graph")
        for source in self.edges:
            print(source,end=" => ")
            for target in self.edges[source]:
                print(target,end=" ")
            print()

    def BfsUtil(self,source,visited):
        queue = []
        queue.append(source)
        visited[source] = "Blue"
        while(queue != []):
            source  = queue.pop(0)
            color = visited[source]
            for target in self.edges.get(source,[]):
                if visited[target] is None:
                    visited[target] = ("Blue","Green")[color == "Blue"]
                    queue.append(target)
                elif visited[target] == color:
                    return False
        # print(visited)
        return True

    # Using BFS
    def isBipartiteGraphUsingBFS(self):
        visited = [None]*self.count
        for i in range(self.count):
            if visited[i] is None:
                ans = self.BfsUtil(i,visited)
                if not ans:
                    return False
        return True
        
    
    def DfsUtil(self,source,visited,color):
        if visited[source] is None:
            visited[source] = color
        elif visited[source] != color:
            return False
        ans = True
        for vertex in self.edges.get(source,[]):
            mirror = ("Blue","Green")[color == "Blue"]
            if visited[vertex] is None:
                ans &= self.DfsUtil(vertex,visited,mirror)
            elif visited[vertex] == color:
                return False
            if not ans:
                return False
        return True
        
    def isBipartiteGraphUsingDFS(self):
        visited = [None]*self.count
        for i in range(self.count):
            if visited[i] is None:
                ans = self.DfsUtil(i,visited,"Blue")
                # print(visited)
                if not ans:
                    return False
        return True


if __name__ == "__main__":
    g = Graph(4)
    g.addEdge(0,1)
    g.addEdge(0,3)
    g.addEdge(1,2)
    g.addEdge(2,3)
    g.addEdge(3,3)
    print("Is Bipartite Graph using BFS - ",g.isBipartiteGraphUsingBFS())
    print("Is Bipartite Graph using DFS - ",g.isBipartiteGraphUsingDFS())



            
