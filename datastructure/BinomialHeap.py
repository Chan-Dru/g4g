import sys

class BinomialTree:
    def __init__(self,v):
        self.key = v
        self.parent = None
        self.children = []
        self.order = 0

    def add_at_end(self,v):
        v.parent = self
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

    def printNode(self, tree):
        print(tree.key, end=" ")
        if tree.parent is None:
            parent = "N"
        else:
            parent = tree.parent.key
        # parent =(tree.parent.key,"N")[tree.parent is None] 
        print("({}) ".format(parent), end=" ")
        for child in tree.children:
            self.printNode(child)


    def printHeap(self):
        print("Print Heap : ",end = "")
        for tree in self.trees:
            self.printNode(tree)
        print()

    def findNode(self, tree, key):
        queue = [tree]
        while(len(queue)):
            tree = queue.pop(0)
            if(tree.key==key):
                return tree
            for child in tree.children:
                queue.append(child)


    def decreaseKey(self, key, new_value):

        for tree in self.trees: #sibling trees
            tree_node = self.findNode(tree, key)

            if tree_node is not None:
                # print(tree_node, tree_node.key,tree_node.parent.key)     
                tree_node.key = new_value
                parent = tree_node.parent
                while(parent is not None and tree_node.key < parent.key):
                    parent.key, tree_node.key = tree_node.key, parent.key 
                    tree_node = parent
                    parent = parent.parent

    def deleteKey(self, key):
        self.decreaseKey(key,-sys.maxsize)
        self.extractMin()

            
        


if __name__ == "__main__":
    heap = BinomialHeap()
    print("Insert 1 to 15 in Binomial Heap")
    [heap.insert(i) for i in range(15,0,-1)]
    # print([heap.extractMin() for i in range(8)])
    heap.printHeap()
    print("Decrease key of value 15 to 0 in Binomial Heap")
    heap.decreaseKey(15,0)
    heap.printHeap()
    print("Delete key 0 in Binomial Heap")
    heap.deleteKey(0)
    heap.printHeap()