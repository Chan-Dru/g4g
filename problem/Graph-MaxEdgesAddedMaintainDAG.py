from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)

    def addEdges(self,u,v):
        self.edges[u].append(v)
    
    def printEdges(self):
        print("Edges in the graph: ")
        for sourceVertex in self.edges:
            print(sourceVertex," => ",end="")
            for vertex in self.edges[sourceVertex]:
                print(vertex,end=" ")
            print()

    def topologicalSortUtil(self,sourceVertex,visited,stack):
        visited[sourceVertex] = True
        for vertex in self.edges.get(sourceVertex,[]):
            if not visited[vertex]:
                self.topologicalSortUtil(vertex,visited,stack)
        stack.insert(0,sourceVertex)

    # maintain DAG
    def maximizeEdges(self):
        stack = []
        visited = [False]*self.count
        sourceVertex = 0
        for sourceVertex in range(self.count):
            if not visited[sourceVertex]:
                self.topologicalSortUtil(sourceVertex,visited,stack)
        # print(stack)

        edges = []
        for i in range(len(stack)-1):
            sourceVertex = stack[i]
            for vertex in stack[i+1:]:
                if vertex not in self.edges[sourceVertex]:
                    edges.append([sourceVertex,vertex])

        return edges

if __name__ == "__main__":
    g = Graph(6)
    g.addEdges(5, 2); 
    g.addEdges(5, 0); 
    g.addEdges(4, 0); 
    g.addEdges(4, 1); 
    g.addEdges(2, 3); 
    g.addEdges(3, 1);
    g.printEdges()
    print("Maximum edges can be added to DAG is {}".format(g.maximizeEdges()))


