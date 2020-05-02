from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.graph = []
        self.edges = defaultdict(list)

    def addEdge(self,u,v,w=0):
        self.edges[u].append([v,w])
        self.edges[v].append([u,w])
        self.graph.append([u,v,w])

    def printEdges(self):
        print("Print edges of graph")
        for source in self.edges:
            print(source,end=" => ")
            for edge in self.edges[source]:
                print("{} ({})".format(edge[0],edge[1]),end=" ")
            print()

    def IsBipartiteGraphUsingBFS(self,source,visited):
        queue = []
        queue.append(source)
        visited[source] = "Blue"
        while queue != []:
            source = queue.pop(0)
            for edge in self.edges.get(source,[]):
                target = edge[0]
                color = ("Blue","Green")[visited[source]=="Blue"]
                if visited[target] is None:
                    visited[target] = color
                    queue.append(target)
                elif visited[target] != color:
                    return False
        return True

    def IsBipartiteGraph(self):
        visited = [None]*self.count
        for i in range(self.count):
            if visited[i] is None:
                if self.IsBipartiteGraphUsingBFS(i,visited) == False:
                    return False
        return True

    def IsOddLengthCycle(self):
        psudoVertex = self.count
        # add psudo vertex if edge weight is even
        g = Graph(self.count)
        for edge in self.graph:
            source, target, weight = edge
            if weight%2 == 0:
                g.addEdge(source,psudoVertex,1)
                g.addEdge(psudoVertex,target,1)
                psudoVertex += 1
            else:
                g.addEdge(source,target,1)
        g.count = psudoVertex
        print("Transformed Graph with psudo vertex")
        g.printEdges()

        return not g.IsBipartiteGraph()

if __name__ == "__main__":
    graph = Graph(5)
    graph.addEdge(1,2,12)
    graph.addEdge(2,3,1)
    graph.addEdge(4,3,2)
    graph.addEdge(4,1,20)
    graph.printEdges()
    print("Is graph with odd length cycle -",graph.IsOddLengthCycle())

        
