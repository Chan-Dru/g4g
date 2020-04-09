# Using Adjacency Matrix
class Graph:
    def __init__(self):
        self.matrix = []
        self.vertex = []
    
    def addVertex(self,v):
        self.vertex.append(v)
        index = len(self.vertex)
        self.matrix.append([0]*index)
        for i in range(index-1):
            self.matrix[i].append(0)
    
    def isVertex(self,v):
        v_index = None
        for i,key in enumerate(self.vertex):
            if key == v:
                v_index = i
        return v_index

    def addEdge(self,v1,v2,e):
        v1_index = self.isVertex(v1)
        v2_index = self.isVertex(v2)
        if v1_index is not None and v2_index is not None:
            self.matrix[v1_index][v2_index] = e
            self.matrix[v2_index][v1_index] = e
    
    def removeVertex(self,v):
        v_index = self.isVertex(v)
        if v_index is not None:
            for i in range(len(self.vertex)):
                del self.matrix[i][v_index]
            del self.matrix[v_index]
            del self.vertex[v_index]

    def removeEdge(self,v1,v2):
        v_connected, v1_index, v2_index = self.isVertexConnected(v1,v2)
        if v_connected:
            self.addEdge(v1,v2,0)
    
    def isVertexConnected(self,v1,v2):
        v1_index = self.isVertex(v1)
        v2_index = self.isVertex(v2)

        if v1_index is not None and v2_index is not None:
            return self.matrix[v1_index][v2_index] > 0,v1_index,v2_index
        else:
            print("Vertex {} {} and {} {}".format(v1,("not exists","exists")[v1_index is not None],v2,("not exists","exists")[v2_index is not None]))
        return False,v1_index,v2_index
        
    
    def getEdges(self):
        edges = []
        for i,row in enumerate(self.matrix):
            for j,col in enumerate(row[i:]):
                if col > 0:
                    edges.append((self.vertex[i],self.vertex[j+i],col))
        return edges

    def getVertices(self):
        return self.vertex
    
    def getGraph(self):
        for row in self.matrix:
            print(row)

if __name__ == "__main__":
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(4)
    g.addVertex(8)
    print("{} are the graph vertices".format(g.getVertices()))
    print("Graph with no Edges only Vertices")
    g.getGraph()
    g.addEdge(2,8,1)
    g.addEdge(2,1,5)
    g.addEdge(4,8,3)
    g.addEdge(1,8,6)
    print("Graph with Edges")
    g.getGraph()
    print("{} are the edges of the graph in (v1,v2,w)".format(g.getEdges()))
    print("Remove the edge in vertex 1 and 8")
    g.removeEdge(1,8)
    print("{} are the graph vertices".format(g.getVertices()))
    g.getGraph()
    print("Remove the vertex 2")
    g.removeVertex(2)
    print("{} are the graph vertices".format(g.getVertices()))
    g.getGraph()