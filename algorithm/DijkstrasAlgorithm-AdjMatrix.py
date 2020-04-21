import sys

class Graph:
    def __init__(self,v):
        self.graph = None
        self.length = v
    
    def printGraph(self):
        for row in self.graph:
            print(row)

    def findmin(self, notVisitedVertex,visitedVertex):
        minWeight = sys.maxsize
        vertex = None
        for i in range(self.length):
            if not visitedVertex[i] and notVisitedVertex[i] < minWeight:
                minWeight = notVisitedVertex[i]
                vertex = i
        return vertex,minWeight

    def shortestPath(self,sourceVertex):
        maxWeight = sys.maxsize
        visitedVertex = [False]*self.length
        notVisitedVertex = [maxWeight]*self.length
        notVisitedVertex[sourceVertex] = 0
        parent = [None]*self.length

        for c in range(self.length):
            sourceVertex, weight = self.findmin(notVisitedVertex,visitedVertex)
            # print(sourceVertex,weight) 
            visitedVertex[sourceVertex] = True
            for edge in range(self.length):
                if self.graph[sourceVertex][edge] > 0 and not visitedVertex[edge] and weight + self.graph[sourceVertex][edge] < notVisitedVertex[edge]:
                        notVisitedVertex[edge] = weight + self.graph[sourceVertex][edge]
                        parent[edge] = sourceVertex
                        # print(edge)
        print("Parent of each vertex {}".format(parent))
        return notVisitedVertex





if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0], 
        [4, 0, 8, 0, 0, 0, 0, 11, 0], 
        [0, 8, 0, 7, 0, 4, 0, 0, 2], 
        [0, 0, 7, 0, 9, 14, 0, 0, 0], 
        [0, 0, 0, 9, 0, 10, 0, 0, 0], 
        [0, 0, 4, 14, 10, 0, 2, 0, 0], 
        [0, 0, 0, 0, 0, 2, 0, 1, 6], 
        [8, 11, 0, 0, 0, 0, 1, 0, 7], 
        [0, 0, 2, 0, 0, 0, 6, 7, 0] 
        ];
    sourceVertex = 0
    # g.printGraph()
    print("Shortest path from vertex {} to others is {}".format(sourceVertex,g.shortestPath(sourceVertex)))
