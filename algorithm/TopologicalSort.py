from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)

    def addEdge(self,u,v,w=0):
        self.edges[u].append([v,w])

    def printGraph(self):
        for u in self.edges:
            print("{} => ".format(u),end="")
            for v in self.edges[u]:
                print("{} ({})".format(v[0],v[1]),end="")
            print()
    
    def topologicalSortUtil(self,source,visited,stack):
        visited[source] = True
        for edge in self.edges.get(source,[]):
            if not visited[edge[0]]:
                self.topologicalSortUtil(edge[0],visited,stack)
        stack.insert(0,source)

    def topologicalSort(self):
        visited = [False]*self.count
        stack = []
        for source in self.edges:
            if not visited[source]:
                self.topologicalSortUtil(source,visited,stack)
        print("Topological Sort of give DAG is {}".format(stack))

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5,0)
    g.addEdge(5,2)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(2,3)
    g.addEdge(3,1)
    g.topologicalSort()




