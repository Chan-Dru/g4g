from Graph import Graph

def SieveOfEratosthenes(n,l=2):
    prime = [True]*n
    p = 2
    while(p*p<=n):
        if prime[p]:
            for i in range(p*p,n,p):
                prime[i] = False
        p += 1
    
    return [i for i in range(l,n) if prime[i]]

def compare(u,v):
    i = str(u)
    j = str(v)
    n = 0
    if i[0] != j[0]:
        n += 1
    if i[1] != j[1]:
        n += 1
    if i[2] != j[2]:
        n += 1
    if i[3] != j[3]:
        n += 1
    return n == 1

class Test(Graph):
    def __init__(self, v, directed=True):
        super().__init__(v, directed)

    def BFS(self,start,end):
        queue = [start]
        visited = [False]*self.length
        visited[start] = 1
        while(len(queue)):
            q = queue.pop(0)
            for i in self.edges[q]:
                if end == i:
                    return visited[q]
                elif not visited[i]:
                    visited[i] = visited[q]+1
                    queue.append(i)
        return None
                

    def shortestPath(self,start,end):
        if start == end:
            return 0
        return self.BFS(start,end)

if __name__ == "__main__":
    # find the 4 digit prime numbers
    prime = SieveOfEratosthenes(9999,1000)
    
    # form the graph with those prime numbers as vertex and form edges if they differ by single digit value
    v = len(prime)
    g = Test(v, False)
    for i in range(v):
        for j in range(v):
            if compare(prime[i],prime[j]):
                g.addEdge(i,j)
    # g.printEdges()

    num1 = 1033
    num2 = 8179
    path = g.shortestPath(prime.index(num1), prime.index(num2))
    print("Shortest Path to traverse from {} to {} is {}".format(num1,num2,path))
    
    
