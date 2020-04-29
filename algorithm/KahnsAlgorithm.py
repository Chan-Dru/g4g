from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)

    def addEdge(self,u,v,w=0):
        self.edges[u].append([v,w])

    # Topological Sort
    def kahnsAlgorithm(self):
        indegree = [0]*self.count
        topologicalSort = []
        count = 0
        queue = []

        # find indegree of each vertex
        for sourceVertex in self.edges:
            for edge in self.edges[sourceVertex]:
                vertex = edge[0]
                indegree[vertex] += 1

        # add motherVertex to queue
        for vertex in range(self.count):
            if indegree[vertex] == 0:
                queue.append(vertex)

        while(queue != []):
            sourceVertex = queue.pop(0)
            count += 1
            topologicalSort.append(sourceVertex)
            for edge in self.edges.get(sourceVertex,[]):
                vertex = edge[0]
                indegree[vertex] -= 1

                if indegree[vertex] == 0:
                    queue.append(vertex)
        
        # print(count,topologicalSort)
        if count != self.count:
            print("Not a Directed Acyclic Graph - Topological Sort can't be found")
        else:
            print("Topological Sort of the given DAG is {}".format(topologicalSort))

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5,0)
    g.addEdge(5,2)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(2,3)
    g.addEdge(3,1)
    g.addEdge(1,2)
    g.kahnsAlgorithm()

        
