from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)
        self.graph = []

    def addEdge(self,u,v,w):
        self.edges[u].append([v,w])
        self.graph.append([u,v,w])
    
    def dfs_util(self,source,visited,stack):
            visited[source] = True
            for edge in self.edges.get(source,[]):
                target, weight = edge
                if not visited[target]:
                    self.dfs_util(target,visited,stack)
            stack.insert(0,source)

    def topologicalSort(self):
        stack = []
        source =1
        visited = [False]*self.count
        for source in range(1,self.count):
            if not visited[source]:
                self.dfs_util(source,visited,stack)
        print(stack)
        return stack

    def longestPath(self):
        pathWeight = [0]*self.count
        vertexSorted = self.topologicalSort()
        for source in vertexSorted:
            for edge in self.edges.get(source,[]):
                target ,weight = edge
                if pathWeight[target] < pathWeight[source]+weight:
                    pathWeight[target] = pathWeight[source]+weight
        print(pathWeight)
        return max(pathWeight)

if __name__ == "__main__":
    g = Graph(7)
    g.addEdge(1,2,3) 
    g.addEdge(2,3,4)
    g.addEdge(2,6,2)
    g.addEdge(4,6,6)
    g.addEdge(5,6,5)
    print("Longest Path length is {}".format(g.longestPath()))