class AdjNodes:
    def __init__(self,vertex,weight=None):
        self.vertex = vertex
        self.weight = weight
        self.next = None

class Graph(AdjNodes):
    def __init__(self):
        self.vertex = []
    
    def addVertex(self,v):
        self.vertex.append(AdjNodes(v))

    def getVertices(self):
        return [node.vertex for node in self.vertex]

    def isVertex(self,v):
        for i in range(len(self.vertex)):
            if v == self.vertex[i].vertex:
                return i
        return None

    def isVertexConnected(self,v1,v2):
        v1_index = self.isVertex(v1) 
        v2_index = self.isVertex(v2)


    def addEdge(self,v1,v2,w):
        v1_index = self.isVertex(v1) 
        v2_index = self.isVertex(v2)

        if v1_index is not None and v2_index is not None:
            src = self.vertex[v1_index]
            dest = self.vertex[v2_index]
            while(src.next != None):
                src = src.next
            src.next = AdjNodes(v2,w)
            while(dest.next != None):
                dest = dest.next
            dest.next = AdjNodes(v1,w)

    def getGraph(self):
        for node in self.vertex:
            print(node.vertex,end=" ")
            while(node.next != None):
                print("-->",node.next.vertex,end= " ")
                node = node.next
            print()

    def removeVertex(self,v):
        v_index = self.isVertex(v)
        if v_index is not None:
            node = self.vertex[v_index]
            while(node.next is not None):
                self.removeEdge(node.next.vertex,v,False)
                node = node.next
            del self.vertex[v_index]

    def removeEdge(self,v1,v2,flag=True):
        v1_index = self.isVertex(v1)
        v2_index = self.isVertex(v2)
        if v1_index is not None and v2_index is not None:
            node = self.vertex[v1_index]
            while(node.next is not None and node.next.vertex != v2):
                node = node.next
            if node.next is not None:
                node.next = node.next.next
            else:
                node.next = None
            if flag:
                node = self.vertex[v2_index]
                while(node.next is not None and node.next.vertex != v1):
                    node = node.next
                if node.next is not None:
                    node.next = node.next.next
                else:
                    node.next = None

if __name__ == "__main__":
    g = Graph()
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(4)
    g.addVertex(8)
    print("{} are the graph vertices".format(g.getVertices()))
    print("Graph with no Edges only vertices")
    g.getGraph()
    g.addEdge(2,8,1)
    g.addEdge(2,1,5)
    g.addEdge(4,8,3)
    g.addEdge(1,8,6)
    print("Graph with Edges")
    g.getGraph()
    print("Remove the edge in vertex 1 and 8")
    g.removeEdge(1,8)
    g.getGraph()
    print("Remove the vertex 8")
    g.removeVertex(8)
    g.getGraph()
