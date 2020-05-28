class TrieNode():
    def __init__(self):
        self.children = [None]*26 
        self.isEnd = False

class Trie(TrieNode):
    def __init__(self,):
        self.root = self.getNode()

    def getNode(self):
        return TrieNode()

    def charToIndex(self,ch):
        return ord(ch) - ord('a')
    
    def insert(self,key):
        pcrawl = self.root
        for ch in key:
            index = self.charToIndex(ch)
            if pcrawl.children[index] is None:
                pcrawl.children[index] = self.getNode()
            pcrawl = pcrawl.children[index]
        pcrawl.isEnd = True

    def search(self,key):
        pcrawl = self.root
        for ch in key:
            index = self.charToIndex(ch)
            if pcrawl.children[index] is None:
                return False
            pcrawl = pcrawl.children[index]
        return pcrawl.isEnd

if __name__ == "__main__":
    keys = ["the","a","there","anaswe","any", "by","their"] 
    output = ["Not present in trie", "Present in trie"] 
  
    # Trie object 
    t = Trie() 
  
    # Construct trie 
    for key in keys: 
        t.insert(key) 
  
    # Search for different keys 
    print("{} ---- {}".format("the",output[t.search("the")])) 
    print("{} ---- {}".format("these",output[t.search("these")])) 
    print("{} ---- {}".format("their",output[t.search("their")])) 
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))