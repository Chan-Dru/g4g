from Graph import Graph

class Test(Graph):
    def __init__(self,v,directed=True):
        super().__init__(v,directed)

    def dfs_util(self,start,visited):
        visited[start] = "grey"
        for i in self.edges.get(start,[]):
            if visited[i] == "white":
                self.dfs_util(i,visited)
            elif visited[i]:
                print("Cycle found at ",i)
        visited[start] = "black"

    def DetectCycle(self):
        visited = ["white"]*self.length
        for i in self.edges:
            if visited[i] == "white":
                self.dfs_util(i,visited)
            

if __name__ == "__main__":
    g = Test(5)
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 2) 
    g.addEdge(2, 0) 
    g.addEdge(2, 3) 
    g.addEdge(3, 3)
    # g.addEdge(0, 2) 
    # g.addEdge(1, 2) 
    # g.addEdge(2, 4) 
    # g.addEdge(2, 3) 
    g.printEdges()
    # g.printGraph()
    g.DetectCycle()
