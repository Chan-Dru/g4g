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
        print("\nInorderTraversal without recurssion :")
        self.inorder_norecurrsion(self.root)

    def preorderTraversal(self):
        self.preorder(self.root)
        print("\nPreorderTraversal without recurssion :")
        self.preorder_norecurrsion(self.root)

    def postorderTraversal(self):
        self.postorder(self.root)
        print("\nPostorderTraversal without recurssion :")
        self.postorder_norecurrsion(self.root)

    def levelorderTraversal(self):
        self.levelorder(self.root)
        
    def inorder(self,root):
        if root != None:
            self.inorder(root.left)
            print(root.key, end=" ")
            self.inorder(root.right)

    def inorder_norecurrsion(self,root):
        stack =[root]
        def stackit(current):
            while(current is not None):
                stack.append(current)
                current = current.left
        
        current = stack.pop()
        stackit(current)

        while(len(stack)):
            current = stack.pop()
            print(current.key, end = " ")
            if current.right is not None:
                stackit(current.right)
    
    def preorder(self,root):
        if root != None:
            print(root.key, end = " ")
            self.preorder(root.left)
            self.preorder(root.right)

    def preorder_norecurrsion(self,root):
        stack = [root]
        def stackit(current):
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
        while(len(stack)):
            current = stack.pop()
            print(current.key,end=" ")
            stackit(current)

    def postorder(self,root):
        if root != None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key, end = " ")

    def postorder_norecurrsion(self,root):
        stack1 = [root]
        stack2 = []

        while(len(stack1)):
            current = stack1.pop()
            stack2.append(current.key)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)

        while(len(stack2)):
            print(stack2.pop(),end=" ")

    def getHeight(self):
        return self.height(self.root)

    def height(self,root):
        if root == None:
            return 0
        else:
            leftHeight = self.height(root.left)
            rightHeight = self.height(root.right)
            if leftHeight > rightHeight:
                return leftHeight + 1
            else:
                return rightHeight + 1

    def levelorder(self,root):
        height = self.getHeight()
        for i in range(height):
            self.givenlevelorder(root,i)

    def levelorderusingqueue(self):
        queue = []
        queue.append(self.root)
        while(len(queue)):
            root = queue.pop(0)
            print(root.key, end=" ")
            if root.left != None:
                queue.append(root.left)
            if root.right != None:
                queue.append(root.right)

    def givenlevelorder(self,root,level):
        if root == None:
            return 
        if level == 0:
            print(root.key, end = " ")
        elif level > 0:
            self.givenlevelorder(root.left, level-1)
            self.givenlevelorder(root.right, level-1)
    
    def search(self,i):
        return self.searchTree(self.root,i)

    def searchTree(self,root,i):
        if root == None:
            return None
        else:
            if root.key == i:
                return root
            elif i<root.key:
                return self.searchTree(root.left,i)
            else:
                return self.searchTree(root.right,i)
    
    def delete(self,i):
        self.deleteNode(self.root,i)

    def deleteNode(self,root,i):
        if root is None:
            return root
        if i < root.key:
            root.left = self.deleteNode(root.left,i)
        elif i > root.key:
            root.right = self.deleteNode(root.right,i)
        elif i == root.key:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minvalue(root.right)
            root.key = temp.key
            root.right = self.deleteNode(root.right,temp.key)
        return root

    def minvalue(self,root):
        while(root.left):
            root = root.left
        return root



if __name__ == "__main__":
    arr = [4,7,2,1,5,6,3,8,0,9]
    print(arr)
    tree = BinarySerachTree(arr)
    tree.createTree()
    print("Inorder Traversal : ")
    tree.inorderTraversal()
    print("\nPreorder Traversal : ")
    tree.preorderTraversal()
    print("\nPostorder Traversal : ")
    tree.postorderTraversal()
    print("\nTree height is {}".format(tree.getHeight()))
    print("Levelorder Traversal : ")
    tree.levelorderTraversal()
    print("\nLevelorder Traversal using queue method : ")
    tree.levelorderusingqueue()
    key = 9
    print("\nSearch Tree for the key {} and node is {} ".format(key,tree.search(key)))
    tree.delete(2)
    tree.levelorderusingqueue()
