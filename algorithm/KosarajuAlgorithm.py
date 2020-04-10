import copy
class Graph:
    def __init__(self,v):
        self.length = v
        self.vertex = dict()
        for i in range(v):
            self.vertex[i]=[]
    
    def printGraph(self):
        for i in range(self.length):
            print(i,self.vertex[i])

    def addEdge(self,u,v):
        self.vertex[u].append(v)

    def DFS_util(self,start,visited):
        visited[start] = True
        for i in self.vertex[start]:
            if not visited[i]:
                self.DFS_util(i,visited)
        print(start,end=" ")

    def fill_order(self,start,visited,stack):
        visited[start] = True
        for i in self.vertex[start]:
            if not visited[i]:
                self.fill_order(i,visited,stack)
        stack.append(start)

    def transposeGraph(self):
        tg = Graph(self.length)
        for u in self.vertex:
            for v in self.vertex[u]:
                tg.addEdge(v,u)
        return tg

    def DFS(self):
        visited = [False]*self.length
        for start in range(self.length):
            if not visited[start]:
                print("\nDFS ",start)
                self.DFS_util(start,visited)

    def BFS_util(self,start,visited):
        queue = [start]
        while(queue):
            start = queue.pop(0)
            visited[start]=True
            print(start,end=" ")
            for i in self.vertex[start]:
                if not visited[i]:
                    queue.append(i)

    def BFS(self):
        visited = [False]*self.length
        for start in range(self.length):
            if not visited[start]:
                print("\nBFS ",start)
                self.BFS_util(start,visited)

    def SCG(self):
        stack = []
        visited = [False]*self.length
        for i in range(self.length):
            if not visited[i]:
                self.fill_order(i,visited,stack)
        print("DFS Filled Stack ",stack)

        tg = self.transposeGraph()
        print("Transposed Graph")
        tg.printGraph()

        visited = [False]*tg.length
        while(stack):
            i = stack.pop()
            if not visited[i]:
                print("\n", i,"=>")
                # tg.DFS_util(i,visited)
                tg.BFS_util(i,visited)

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
    g.printGraph()
    # g.BFS()
    # g.DFS()
    g.SCG()

