from collections import defaultdict

class Graph:
    def __init__(self,v):
        self.count = v
        self.edges = defaultdict(list)

    def addEdge(self,u,v,w=0):
        self.edges[u].append([v,w])

    def allTopologicalSortUtil(self,visited,indegree,stack):
        flag = False
        for source in range(self.count):
            if not visited[source] and indegree[source] == 0:
                visited[source] = True
                
                stack.append(source)
                
                for edge in self.edges.get(source,[]):
                    indegree[edge[0]] -= 1
                
                self.allTopologicalSortUtil(visited,indegree,stack)

                visited[source] = False
                
                stack.pop(len(stack)-1)

                for edge in self.edges.get(source,[]):
                    indegree[edge[0]] += 1
                
                flag = True
        
        if not flag:
            print(stack)

    def allTopologicalSort(self):
        visited = [False]*self.count
        indegree = [0]*self.count
        stack = []

        for source in self.edges:
            for edge in self.edges[source]:
                indegree[edge[0]] += 1

        self.allTopologicalSortUtil(visited,indegree,stack)

if __name__ == "__main__":
    g = Graph(6)
    g.addEdge(5,0)
    g.addEdge(5,2)
    g.addEdge(4,0)
    g.addEdge(4,1)
    g.addEdge(2,3)
    g.addEdge(3,1)
    g.allTopologicalSort()
