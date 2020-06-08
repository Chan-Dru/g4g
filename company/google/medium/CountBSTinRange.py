"""
Input:
        10
      /    \
    5       50
   /       /  \
 1       40   100
Range: [5, 45]

Output:  3
There are three nodes in range, 5, 10 and 40
"""

class Node():
    def __init__(self, value):
        self.value = value
        self.left = self.right = None

class BST(Node):
    def __init__(self):
        self.root = None
        self.length = 0
    
    def insertNode(self,root,value):
        if root is None:
            return Node(value)
        else:
            if value < root.value:
                if root.left is None:
                    root.left = Node(value)
                else:
                    return self.insertNode(root.left, value)
            else:
                if root.right is None:
                    root.right = Node(value)
                else:
                    return self.insertNode(root.right,value)

    def insert(self,value):
        if self.root is None:
            self.root = Node(value)
            return 
        
        self.insertNode(self.root,value)

        
    
    def inorder(self,root,output):
        if root is not None:
            self.inorder(root.left,output)
            output.append(root.value)
            self.inorder(root.right,output)


    def printBST(self,output):
        self.inorder(self.root,output)

if __name__ == "__main__":
    tree = BST()
    tree.insert(10)
    tree.insert(5)
    tree.insert(1)
    tree.insert(50)
    tree.insert(40)
    tree.insert(100)
    
    low,high = (5,45)
    count = 0
    
    output = []
    tree.printBST(output)
    print(output)
    
    for i in output:
        if low <= i <= high:
            print(i,end=" ")
            count = count + 1
    print("=>",count)
