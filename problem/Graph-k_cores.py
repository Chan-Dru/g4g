from Graph import Graph

class Test(Graph):
    def __init__(self,v,directed=True):
        super().__init__(v,directed)

    def removeEdges(self,u):
        for v in self.edges[u]:
            self.edges[v].remove(u)

    def k_cores(self,n):
        flag = True
        sorted_vertex = sorted(self.edges,key=lambda x:len(self.edges[x]))
        while(flag):
            flag = False
            removeVertex = []
            for u in sorted_vertex:
                if len(self.edges[u]) < n: # vertex less than given cores
                    self.removeEdges(u)
                    removeVertex.append(u)
                    flag = True
            for u in removeVertex:
                del self.edges[u]
                sorted_vertex.remove(u)

    def dfs_util(self,start,visited,k_cores,n):
        visited[start] = True
        
        for v in self.edges[start]:
            if k_cores[start] < n:
                k_cores[v] -= 1

            if not visited[v]:
                if self.dfs_util(v,visited,k_cores,n):
                    k_cores[start] -= 1
    
        return k_cores[start] < n

    def k_cores_using_dfs(self,n):
        visited = [False]*self.length
        v_cores = [len(self.edges[i]) for i in self.edges]

        start = 0
        self.dfs_util(start,visited,v_cores,n)

        for u in self.edges:
            if not visited[u]:
                self.dfs_util(u,visited,v_cores,n)

        for u in self.edges:
            if v_cores[u] >= n:
                print(u," => ",end="")
                for v in self.edges[u]:
                    if v_cores[v] >= n:
                        print(v," ",end=" ")
                print()


if __name__ == "__main__":
    g = Test(9,False)
    g.addEdge(0,1)
    g.addEdge(0,2)
    g.addEdge(1,2)
    g.addEdge(1,5)
    g.addEdge(2,3)
    g.addEdge(2,4)
    g.addEdge(2,5)
    g.addEdge(2,6)
    g.addEdge(3,4)
    g.addEdge(3,6)
    g.addEdge(3,7)
    g.addEdge(4,6)
    g.addEdge(4,7)
    g.addEdge(5,6)
    g.addEdge(5,8)
    g.addEdge(6,7)
    g.addEdge(6,8)

    g.printEdges()
    # g.k_cores(3)
    # g.printEdges()
    g.k_cores_using_dfs(3)