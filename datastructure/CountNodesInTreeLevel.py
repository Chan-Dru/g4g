class Graph():
    def __init__(self,v):
        self.vertex = dict()
        self.length = v
        self.output = []
        for i in range(self.length+1):
            self.vertex[i] = []
    
    def addEdge(self,u,v):
        self.vertex[u].append(v)
        self.vertex[v].append(u)

    def getGraph(self):
        for vertex in self.vertex.keys():
            print(vertex,self.vertex[vertex])

    def BFS_util(self,queue,visited,level,depth):
        if len(queue)>0 and level <= depth:
            start = queue.pop(0)
            if level==depth:
                self.output.append(start)
            visited[start]=True
            for i in self.vertex[start]:
                if visited[i] == False:
                    queue.append(i)
                    self.BFS_util(queue,visited,level+1,depth)
            

    def BFS(self,start,depth):
        visited = [False]*(self.length+1)
        level = 0
        queue = [start]
        self.BFS_util(queue,visited,level,depth)
        print(len(self.output))


if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,3)
    g.addEdge(1,4)
    g.addEdge(1,5)
    g.addEdge(2,6)
    # g.getGraph()
    g.BFS(0,2)