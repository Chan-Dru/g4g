from collections import defaultdict

class Subset:
    def __init__(self,parent,rank):
        self.rank = rank
        self.parent = parent

class UnionFind(Subset):
    def __init__(self,v):
        self.count = v
        self.subsets = [Subset(i,0) for i in range(v)]
    
    def findSet(self,node):
        if self.subsets[node].parent != node:
            self.subsets[node].parent = self.findSet(self.subsets[node].parent)            
        return self.subsets[node].parent

    def isSameSet(self,source,target):
        return self.findSet(source) == self.findSet(target)
    
    def unionSet(self,source,target):
        print("Union of source {} and target {}".format(source,target))
        sourceSet = self.findSet(source)
        targetSet = self.findSet(target)
        if self.subsets[sourceSet].rank < self.subsets[targetSet].rank:
            self.subsets[sourceSet].parent = targetSet
        elif self.subsets[sourceSet].rank > self.subsets[targetSet].rank:
            self.subsets[targetSet].parent = sourceSet
        else:
            self.subsets[targetSet].parent = sourceSet
            self.subsets[targetSet].rank += 1

    def printSet(self):
        print("Print the UnionFind Subsets")
        for i in range(self.count):
            print("{} => {}".format(i,self.subsets[i].parent))


if __name__ == "__main__":
    uf = UnionFind(3)
    uf.printSet()
    print("IsSameSet ",uf.isSameSet(0,1))
    uf.unionSet(0, 1)  
    uf.printSet()
    print("IsSameSet ",uf.isSameSet(1,2))
    uf.unionSet(1, 2) 
    uf.printSet()
    print("IsSameSet ",uf.isSameSet(0,2))
    uf.unionSet(0, 2) 
    uf.printSet()
