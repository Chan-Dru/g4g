class Node:
    def __init__(self,key):
        self.key = key
        self.left = self.right = None

class BinarySerachTree(Node):
    def __init__(self,arr):
        self.root = None
        self.arr = arr
    
    def createTree(self):
        self.root = self.insertNode(self.root, self.arr[0])
        for i in self.arr[1:]:
            self.insertNode(self.root, i)

    def insertNode(self, root, i):
        if root == None:
            return Node(i)
        else:
            if i < root.key:
                if root.left == None:
                    root.left = Node(i)
                else:
                    return self.insertNode(root.left, i)
            else:
                if root.right == None:
                    root.right = Node(i)
                else:
                    return self.insertNode(root.right, i)

    def inorderTraversal(self):
        self.inorder(self.root)
        
    def inorder(self,root):
        if root != None:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

if __name__ == "__main__":
    arr = [4,7,2,1,8,3,0,9,5]
    print(arr)
    tree = BinarySerachTree(arr)
    tree.createTree()
    tree.inorderTraversal()
