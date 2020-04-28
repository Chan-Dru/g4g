from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)
        self.undirectedEdges = []

    def addEdges(self,u,v):
        self.edges[u].append(v)

    def printEdges(self):
        print("Edges in the Graph:")
        for sourceVertex in self.edges:
            print("{} => ".format(sourceVertex),end="")
            for edge in self.edges[sourceVertex]:
                print(edge,end=" ")
            print()
    
    def addUnDirectedEdges(self,u,v):
        self.undirectedEdges.append([u,v])

    def assignEdgeDirection(self):
        vertexSort = self.topologicalSort()
        # print(vertexSort)
        for edge in self.undirectedEdges:
            u,v = edge
            u_index = vertexSort.index(u)
            v_index = vertexSort.index(v)
            if u_index < v_index:
                self.addEdges(u,v)
            else:
                self.addEdges(v,u)
        
        self.undirectedEdges = []

    def topologicalSortUtil(self,start,stack,visited):
        visited[start] = True
        for end in self.edges.get(start,[]):
            if not visited[end]:
                self.topologicalSortUtil(end,stack,visited)
        stack.insert(0,start)

    def topologicalSort(self):
        visited = [False]*self.count
        stack = []
        for sourceVertex in self.edges:
            if not visited[sourceVertex]:
                self.topologicalSortUtil(sourceVertex,stack,visited)
        return stack

if __name__ == "__main__":
    g = Graph(6)
    g.addEdges(0,5)
    g.addEdges(0,1)
    g.addEdges(5,1)
    g.addEdges(5,2)
    g.addEdges(1,2)
    g.addEdges(1,3)
    g.addEdges(1,4)
    g.addEdges(2,3)
    g.addEdges(2,4)
    g.addEdges(3,4)
    # print(g.topologicalSort())
    g.printEdges()
    print("Add UnDirectedEges in DAG, assign direction and remain DAG")
    g.addUnDirectedEdges(3,0)
    g.addUnDirectedEdges(0,2)
    g.addUnDirectedEdges(4,5)
    g.assignEdgeDirection()
    g.printEdges()
