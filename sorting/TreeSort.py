class Node:
    def __init__(self,key):
        self.key = key
        self.left = self.right= None

class BinarySearchTree(Node):
    def __init__(self,arr):
        self.root = None
        self.arr = arr
        self.createTree()
    
    def insertNode(self,root,key):
        if root is None:
            return Node(key)
        else:
            if key < root.key:
                if root.left == None:
                    root.left = Node(key)
                else:
                    return self.insertNode(root.left,key)
            else:
                if root.right == None:
                    root.right = Node(key)
                else:
                    return self.insertNode(root.right,key)

    def createTree(self):
        self.root = self.insertNode(self.root,arr[0])
        for i in self.arr[1:]:
            self.insertNode(self.root,i)
    
    def sort(self):
        return [i for i in self.inorder(self.root)]
            
# with recurssion
    # def inorder(self,root):
    #     if root != None:
    #         self.inorder(root.left)
    #         print(root.key)
    #         self.inorder(root.right)

# without recursion
    def inorder(self,root):
        stack = [root]
        def stackit(current):
            while(current is not None):
                stack.append(current)
                current = current.left
        
        current = stack.pop()
        stackit(current)

        while(len(stack)):
            current = stack.pop()
            yield current.key
            if current.right != None:
                stackit(current.right)
            


def TreeSort(arr):
    tree = BinarySearchTree(arr)
    return tree.sort()
    

if __name__ == "__main__":
    arr = [3,5,1,7,2,8,4,6,9,0]
    print(arr)
    arr = TreeSort(arr)
    print("Sorted array is {}".format(arr))