"""
Input : dict = {"ale", "apple", "monkey", "plea"}   
        str = "abpcplea"  
Output : apple 

Input  : dict = {"pintu", "geeksfor", "geeksgeeks", 
                                        " forgeek"} 
         str = "geeksforgeeks"
Output : geeksgeeks
"""

def isSubsequence(item, word):
    m = len(item)
    n = len(word)
    i = j = 0
    while i < m and j < n:
        if item[i] == word[j]:
            i = i + 1
        j = j + 1
    return i == m 

def largestWord(word, dictionary):
    result = ""
    for item in dictionary:
        if len(item) > len(result) and isSubsequence(item,word):
            result = item
    return result
    

if __name__ == "__main__":
    dictionary = {"ale", "apple", "monkey", "plea"}   
    word = "abpcplea"

    print(largestWord( word, dictionary))


