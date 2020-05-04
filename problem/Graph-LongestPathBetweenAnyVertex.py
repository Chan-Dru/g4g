from collections import defaultdict

# works for both non cyclic graph - directed / undirected
class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)
        self.graph = []

    def addEdge(self,u,v,w):
        self.edges[u].append([v,w])
        self.edges[v].append([u,w])
        self.graph.append([u,v,w])
    
    def dfs_util(self,source,visited,previousWeight,pathWeight):
            visited[source] = True
            currentWeight = 0
            for edge in self.edges.get(source,[]):
                target, weight = edge
                if visited[target] is None:
                    currentWeight = previousWeight + weight
                    self.dfs_util(target,visited,currentWeight,pathWeight)
                if currentWeight > pathWeight[0]:
                    pathWeight[0] = currentWeight
                currentWeight = 0

    def longestPath(self):
        pathWeight = [0]
        for source in range(self.count):
            visited = [None]*self.count
            if visited[source] is None:
                self.dfs_util(source,visited,0,pathWeight)
                # print(source,pathWeight)
        return pathWeight[0]

if __name__ == "__main__":
    g = Graph(7)
    g.addEdge(1,2,3) 
    g.addEdge(2,3,4)
    g.addEdge(2,6,2)
    g.addEdge(4,6,6)
    g.addEdge(5,6,5)
    print("Longest Path length is {}".format(g.longestPath()))
