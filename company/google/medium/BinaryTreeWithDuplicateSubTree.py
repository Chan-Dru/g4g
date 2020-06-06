"""
Input :  Binary Tree 
               A
             /    \ 
           B        C
         /   \       \    
        D     E       B     
                     /  \    
                    D    E
Output : Yes
"""
class Node():
    def __init__(self,value):
        self.value = value
        self.left = self.right = None

def dubsubutil(root,subtrees):
    s = ""
    if root is None:
        return s+"$"
    lstr = dubsubutil(root.left,subtrees)
    if lstr == s:
        return s
    rstr = dubsubutil(root.right,subtrees)
    if rstr == s:
        return s
    # print(root.value,s,lstr,rstr)
    s = s + root.value+ lstr +rstr
    if len(s) > 3 and s in subtrees:
        # print("Found ",s)
        return ""

    subtrees.add(s)
    # print(subtrees)
    return s

def dubsub(root):
    subtrees = set()
    if dubsubutil(root,subtrees) == "":
        # print(subtrees)
        return "Yes"
    # print(subtrees)
    return "No"


if __name__ == "__main__":
    root =  Node('A') 
    root.left =  Node('B') 
    root.right =  Node('C') 
    root.left.left =  Node('D') 
    root.left.right =  Node('E') 
    root.right.right =  Node('B') 
    root.right.right.right =  Node('E') 
    # root.right.right.left=  Node('D') 
    
    print(dubsub(root))