import copy

class Graph:
    def __init__(self,v):
        self.length = v
        self.vertex = []
        self.max_int = 99
        for i in range(v):
            self.vertex.append([self.max_int]*v)

    def printGraph(self):
        print("The graph is ")
        for i in self.vertex:
            print(i)

    def addEdge(self,u,v,w):
        self.vertex[u][v] = w

    def findMinPath(self):
        path_graph = copy.deepcopy(self.vertex)
        for k in range(self.length):
            for i in range(self.length):
                for j in range(self.length):
                    if path_graph[i][k] != self.max_int and path_graph[k][j] != self.max_int and path_graph[i][k]+path_graph[k][j] < path_graph[i][j]:
                        # print(i,k,j)
                        path_graph[i][j] = path_graph[i][k]+path_graph[k][j]
        print("Print the Min Path of vertex in Graph - Transitive Closure Matrix")
        for i in path_graph:
            print(i)

if __name__ == "__main__":
    g= Graph(4) 
    g.addEdge(0,1,3)
    g.addEdge(0,3,10)
    g.addEdge(1,2,4)
    g.addEdge(2,3,2)

    g.printGraph()

    g.findMinPath()
