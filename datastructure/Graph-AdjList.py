class AdjNodes:
    def __init__(self,vertex,weight=None):
        self.vertex = vertex
        self.weight = weight
        self.next = None

class Graph(AdjNodes):
    def __init__(self,directed=True):
        self.vertex = []
        self.directed = directed
    
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
            flag = True
            while(src.next != None):
                src = src.next
                # if src.vertex == v2: # check for duplicate node
                #     flag = False
            if flag:
                src.next = AdjNodes(v2,w)
            # For undirected graph
            if not self.directed:
                flag = True
                while(dest.next != None):
                    dest = dest.next
                    # if dest.vertex == v1: # check for duplicate node
                    #     flag = False
                if flag:
                    dest.next = AdjNodes(v1,w)

    def getGraph(self):
        for node in self.vertex:
            print(node.vertex,end=" ")
            while(node.next != None):
                print("-->",node.next.vertex,end= " ")
                node = node.next
            print()

# loop each vertex and remove the edge
    def removeVertex(self,v):
        v_index = self.isVertex(v)
        if v_index is not None:
            for node in self.vertex:
                if node.vertex != v: 
                    self.removeEdge(node.vertex,v)
            del self.vertex[v_index]

    # flag = True For undirected grap flag = False For directed graph
    def removeEdge(self,v1,v2):
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
            if not self.directed:
                node = self.vertex[v2_index]
                while(node.next is not None and node.next.vertex != v1):
                    node = node.next
                if node.next is not None:
                    node.next = node.next.next
                else:
                    node.next = None

    def getVertexNode(self,vertex):
        return self.vertex[self.isVertex(vertex)]

    def BFS(self,start):
        if self.isVertex(start):
            queue = [start]
            visited = []       
            while(len(queue)):
                # print(queue)
                q_node_vertex = queue.pop(0)
                start_node = self.getVertexNode(q_node_vertex)
                print(start_node.vertex, end = " ")
                visited.append(start_node.vertex)
                while(start_node.next is not None):
                    start_node = start_node.next
                    if start_node.vertex not in visited and start_node.vertex not in queue:
                        queue.append(start_node.vertex)

    def DFS_recursive(self,start):
        visited=[]
        start_node = self.getVertexNode(start)
        if self.directed:
            recursive=dict()
            for v in self.vertex:
                recursive[v] = False
            self.DFS_util(start_node,visited,recursive)
        else:
            self.DFS_util(start_node,visited,-1)

    def DFS_util(self,node,visited,recursive):
        if self.directed:
            visited.append(node.vertex)
            recursive[node.vertex]=True
            print(node.vertex,end=" ")
            while(node.next != None):
                node = node.next
                if node.vertex not in visited:
                    self.DFS_util(self.getVertexNode(node.vertex),visited,recursive)
                elif recursive[node.vertex]:
                    print("\ncycle found at ",node.vertex)
            recursive[node.vertex] = False
        else:
            visited.append(node.vertex)
            t = node.vertex
            print(node.vertex,end=" ")
            while(node.next != None):
                node = node.next
                if node.vertex not in visited:
                    self.DFS_util(self.getVertexNode(node.vertex),visited,t)
                elif recursive != node.vertex:
                    print("\ncycle found at ",node.vertex)
            
            

    def DFS(self,start):
        if self.isVertex(start):
            stack = [start]
            visited = []
            parent = []
            while(len(stack)):
                s_node_vertex = stack.pop()
                start_node = self.getVertexNode(s_node_vertex)
                print(start_node.vertex,end=" ")
                visited.append(start_node.vertex)
                head = start_node.vertex
                while(start_node.next is not None):
                    start_node = start_node.next
                    if start_node.vertex not in visited:
                        stack.append(start_node.vertex)
                    elif parent[-1] != start_node.vertex:
                        print()
                        print("parent",parent,"head ",head,"node ",start_node.vertex)
                        print("Visited : ",start_node.vertex in visited)
                        print("In Stack : ",start_node.vertex in stack)
                        print("Cycle found at vertex ",start_node.vertex)
                    else:
                        print("parent skip ",parent,start_node.vertex)
                    print()
                    print("stack ==> ",stack)
                
                if head not in parent:
                    parent.append(head)
if __name__ == "__main__":
    g = Graph(False)
    g.addVertex(0)
    g.addVertex(1)
    g.addVertex(2)
    g.addVertex(3)
    g.addVertex(4)
    g.addVertex(5)
    print("{} are the graph vertices".format(g.getVertices()))
    print("Graph with no Edges only vertices")
    g.getGraph()
    
    g.addEdge(0,2,5)
    g.addEdge(0,1,1)
    g.addEdge(1,2,3)
    g.addEdge(2,0,6)
    g.addEdge(2,3,6)
    g.addEdge(2,4,5)
    g.addEdge(4,5,2)
    g.addEdge(3,3,6)
    g.addEdge(5,0,6)
    print("Graph with Edges")
    g.getGraph()
    # print("Remove the edge in vertex 0 and 2")
    # g.removeEdge(0,2)
    # g.getGraph()
    # print("Remove the vertex 2")
    # g.removeVertex(2)
    # g.getGraph()
    print("Breadth First Search of the Graph")
    g.BFS(2)
    print("\nDepth First Search of the Graph")
    # g.DFS(2)
    g.DFS_recursive(2)
