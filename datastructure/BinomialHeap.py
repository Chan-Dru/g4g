class BinomialTree:
    def __init__(self,v):
        self.key = v
        self.children = []
        self.order = 0

    def add_at_end(self,v):
        self.children.append(v)
        self.order += 1

class BinomialHeap(BinomialTree):
    def __init__(self):
        self.trees = []

    def insert(self,v):
        g = BinomialHeap()
        g.trees.append(BinomialTree(v))
        self.merge(g)
    
    def combine_roots(self,h):
        self.trees.extend(h.trees)
        self.trees.sort(key = lambda tree: tree.order)

    def merge(self,h):
        self.combine_roots(h)
        if len(self.trees) == 0:
            return
        i = 0
        while(i < len(self.trees)-1):
            current = self.trees[i]
            after = self.trees[i+1]
            if current.order == after.order:
                if i+1 < len(self.trees)-1 and after.order == self.trees[i+2].order:
                    after_after = self.trees[i+2]
                    if after.key < after_after.key:
                        after.add_at_end(after_after)
                        del self.trees[i+2]
                    else:
                        after_after.add_at_end(after)
                        del self.trees[i+1]
                else:
                    if current.key < after.key:
                        current.add_at_end(after)
                        del self.trees[i+1]
                    else:
                        after.add_at_end(current)
                        del self.trees[i]
            i += 1
    
    def extractMin(self):
        if len(self.trees) == 0:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        
        self.trees.remove(smallest_node)
        h = BinomialHeap()
        h.trees = smallest_node.children
        self.merge(h)
        return smallest_node.key

    def getMin(self):
        if len(self.trees) == 0:
            return None
        smallest_node = self.trees[0]
        for tree in self.trees:
            if tree.key < smallest_node.key:
                smallest_node = tree
        return smallest_node.key


if __name__ == "__main__":
    heap = BinomialHeap()
    [heap.insert(i) for i in range(15,0,-1)]
    print([heap.extractMin() for i in range(15)])