import math
import sys

class FibonacciTree():
    def __init__(self,key):
        self.key = key
        self.children = []
        self.parent = None
        self.order = 0

    def add_at_end(self,node):
        node.parent = self
        self.children.append(node)
        self.order += 1

class FibonacciHeap(FibonacciTree):
    def __init__(self):
        self.trees = []
        self.least = None
        self.count = 0

    def insert(self,key):
        node = FibonacciTree(key)
        self.trees.append(node)
        self.count += 1
        if self.least is None or key < self.least.key:
            self.least = node
    
    def extractMin(self):
        min_node = self.least
        self.trees.remove(min_node)
        for child in min_node.children:
            child.parent = None
            self.trees.append(child)
        self.count -= 1
        self.least = None
        self.consolidate()
        return min_node.key

    def floor_log2(self,x):
        return math.frexp(x)[1] - 1

    def consolidate(self):
        l = self.floor_log2(self.count) + 1
        aux = [None]*l
        while(self.trees != []):
            x = self.trees.pop(0)
            order = x.order
            while aux[order] is not None:
                y = aux[order]
                if x.key > y.key:
                    x,y = y,x
                x.add_at_end(y)
                aux[order] = None
                order += 1
            
            aux[order] = x

        self.least = None
        for tree in aux:
            if tree is not None:
                self.trees.append(tree)
                if self.least is None or tree.key < self.least.key:
                    self.least = tree
            

    def find_node(self,tree,key):
        queue = [tree]
        while(queue != []):
            tree = queue.pop(0)
            if tree.key == key:
                return tree
            for child in tree.children:
                queue.append(child)

    def decreaseKey(self,key,new_value):
        for tree in self.trees:
            node = self.find_node(tree,key)
            if node is not None:
                parent = node.parent
                node.key = new_value
                while(parent is not None and node.key < parent.key):
                    # self.printHeap()
                    node.key,parent.key = parent.key,node.key
                    node = parent
                    parent = parent.parent

                if node.key < self.least.key:
                    self.least = node

    def deleteKey(self,key):
        for tree in self.trees:
            node = self.find_node(tree,key)
            if node is not None:
                node.key = -sys.maxsize
                self.least = node
                self.extractMin()


    def printTree(self,tree):
        print("{} ({})".format(tree.key,"N" if tree.parent is None else tree.parent.key),end=" ")
        for child in tree.children:
            self.printTree(child)

    def printHeap(self):
        print("Heap nodes : ",end="")
        for tree in self.trees:
            self.printTree(tree)
        print()
        
if __name__ =="__main__":
    heap = FibonacciHeap()
    [heap.insert(x) for x in range(15,0,-1)]
    print("Extract Min from heap => {}".format(heap.extractMin()))
    heap.printHeap()
    print("Decrease key 15 to new value 1")
    heap.decreaseKey(15,1)
    heap.printHeap()
    print("Extract Min from heap => {}".format(heap.extractMin()))
    heap.printHeap()
    print("Delete key 2 from heap")
    heap.deleteKey(2)
    heap.printHeap()
    