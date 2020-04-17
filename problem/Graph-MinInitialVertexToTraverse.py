from Graph import Graph

class Test(Graph):
    def __init__(self,v):
        super().__init__(v)

    def dfs(self,i,j,tc,n):
        tc[i][j] = True
        # print("=>",i,j)
        if (i+1 < n) and (self.graph[i+1][j] <= self.graph[i][j]) and not tc[i+1][j]:
            # print("down")
            self.dfs(i+1,j,tc,n)
        if (i-1 >= 0) and (self.graph[i-1][j] <= self.graph[i][j]) and not tc[i-1][j]:
            # print("up", self.graph[i-1][j] <= self.graph[i][j])
            self.dfs(i-1,j,tc,n)
        if (j+1 < n) and (self.graph[i][j+1] <= self.graph[i][j]) and not tc[i][j+1]:
            # print("right")
            self.dfs(i,j+1,tc,n)
        if (j-1 >= 0) and (self.graph[i][j-1] <= self.graph[i][j]) and not tc[i][j-1]:
            # print("left")
            self.dfs(i,j-1,tc,n)            

    def MinTraversal(self):
        t = []
        tc = [[False for i in range(self.length+2)] for i in range(self.length+2)]
        for i in range(self.length):
            for j in range(self.length):
                t.append([self.graph[i][j], i, j])
    
        g = sorted(t, key = lambda x: x[0],reverse=True) #sort the vertex by value
        # print(g)
        n = self.length
        print("Initial Vertex to traverse the entire graph")
        for vertex in g:
            if not tc[vertex[1]][vertex[2]]:
                print(vertex[1], vertex[2])
                self.dfs(vertex[1],vertex[2],tc,n)


        


if __name__ == "__main__":
    g = Test(3)
    g.addEdge(0, 0, 1)
    g.addEdge(0, 1, 2) 
    g.addEdge(0, 2, 3)
    g.addEdge(1, 0, 2)
    g.addEdge(1, 1, 3) 
    g.addEdge(1, 2, 1) 
    g.addEdge(2, 0, 1) 
    g.addEdge(2, 1, 1) 
    g.addEdge(2, 2, 1)
    g.printGraph()
    # g.printEdges()
    g.MinTraversal()
    # g.PathFinder(5,3)