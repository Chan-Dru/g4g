'''
Input: dictionary[] = ["GEEKS", "FOR", "QUIZ", "GO"];
       boggle[][]   = [['G','I','Z'],
                       ['U','E','K'],
                       ['Q','S','E']];
      isWord(str): returns true if str is present in dictionary
                   else false.

Output:  Following words of the dictionary are present
         GEEKS
         QUIZ
'''


class TrieNode():
    def __init__(self):
        self.child = [None]*26
        self.isEnd = False

class Trie(TrieNode):
    def __init__(self):
        self.root =TrieNode()

    def insert(self,key):
        pcrawl = self.root
        for ch in key:
            index = ord(ch)-ord("A")
            if pcrawl.child[index] is None:
                pcrawl.child[index] = TrieNode()
            pcrawl = pcrawl.child[index]
        pcrawl.isEnd = True

dictionary = ["CAT"]
boggle =  [['C','A','P'],
            ['B','N','D'],
            ['T','A','C']]  

# dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
# boggle =    [['G','I','Z'],
#             ['U','E','K'],
#             ['Q','S','E']]    
l = len(boggle)

def safeword(i,j,visited):
    if i >=0 and i<l and j >= 0 and j < l and visited[i][j] == 0:
        return True
    return False

def findword_util(root,visited,i,j,s):
    if root.isEnd:
        print(s)
    visited[i][j] = 1 
    for m in range(26):
        if root.child[m]:
            ch = chr(m+ord("A"))
            if safeword(i-1, j-1, visited) and boggle[i-1][j-1] == ch:
                findword_util(root.child[m],visited,i-1,j-1,s+ch)
            if safeword(i, j-1, visited) and boggle[i][j-1] == ch:
                findword_util(root.child[m],visited,i,j-1,s+ch)
            if safeword(i+1, j-1, visited) and boggle[i+1][j-1] == ch:
                findword_util(root.child[m],visited,i+1,j-1,s+ch)
            if safeword(i-1, j, visited) and boggle[i-1][j] == ch:
                findword_util(root.child[m],visited,i-1,j,s+ch)
            if safeword(i+1, j, visited) and boggle[i+1][j] == ch:
                findword_util(root.child[m],visited,i+1,j,s+ch)
            if safeword(i-1, j+1, visited) and boggle[i-1][j+1] == ch:
                findword_util(root.child[m],visited,i-1,j+1,s+ch)
            if safeword(i, j+1, visited) and boggle[i][j+1] == ch:
                findword_util(root.child[m],visited,i,j+1,s+ch)
            if safeword(i+1, j+1, visited) and boggle[i+1][j+1] == ch:
                findword_util(root.child[m],visited,i+1,j+1,s+ch)
    visited[i][j] = 0


def findword(T):
    visited = [[0 for i in range(l) ] for i in range(l)]
    pcrawl = T.root
    s = ""
    for i in range(l):
        for j in range(l):
            if pcrawl.child[ord(boggle[i][j]) - ord("A")]:
                s = s + boggle[i][j]
                findword_util(pcrawl.child[ord(boggle[i][j]) - ord("A")], visited, i, j, s)
                s= ""


if __name__ == "__main__":
    # dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    # boggle =    [['G','I','Z'],
    #             ['U','E','K'],
    #             ['Q','S','E']]
    T = Trie()
    for key in dictionary:
        T.insert(key)
    findword(T)