class Graph:
    def __init__(self,v):
        self.length = v
        self.vertex = dict()
        for i in range(self.length):
            self.vertex[i] = []
    
    def printGraph(self):
        for i in range(self.length):
            print(self.vertex[i])

    def addEdge(self,u,v):
        self.vertex[u].append(v)

    def BFS(self,v,visited):
        queue = [v]
        count = 0
        output = []
        while(len(queue)):
            v = queue.pop(0)
            if not visited[v]:
                count += 1
                output.append(v)
                visited[v] = True
                for i in self.vertex[v]:
                    if not visited[i]:
                        queue.append(i)
        print(output)
        return count

    def DFS_util(self,start,visited,output):
        visited[start] = True
        for i in self.vertex[start]:
            if not visited[i]:
                self.DFS_util(i,visited,output)
        print(start,end = " ")
        output.append(start)


            
    # works for directed connected graph, mother vertex is one through which all nodes are reachable
    def motherVertex(self):
        # # sorted vertex by its length , reduces time to find the first Mother vertex
        # key = sorted(self.vertex,key=lambda x :len(self.vertex[x]),reverse=True)
        # # for i in key:
        # for i in range(self.length):
        #     visited = [False]*self.length
        #     self.BFS(i,visited)
        #     # if (self.BFS(i,visited) == self.length):
        #     #     print("The Mother Vertex is {}".format(i))
        #         # break

        # Using Kosaraju's Algorithm
        visited = [False]*self.length
        v = -1
        stack = []
        for i in range(self.length):
            if not visited[i]:
                self.DFS_util(i,visited,stack)
                v = i

        print("\nthe last index",v)
        output = []
        visited = [False]*self.length
        self.DFS_util(v,visited,output)
        if len(output) == self.length:
            print("\nThe Mother Vertex is {}".format(v))
                

if __name__ == "__main__":
    g = Graph(7) 
    g.addEdge(0, 1) 
    g.addEdge(0, 2) 
    g.addEdge(1, 3) 
    g.addEdge(4, 1) 
    g.addEdge(6, 4) 
    g.addEdge(5, 6) 
    g.addEdge(5, 2) 
    g.addEdge(6, 0)
    # g.printGraph()
    g.motherVertex()