"""
Operations - Insert, Remove, Replace

Input:   str1 = "geek", str2 = "gesek"
Output:  1
We can convert str1 into str2 by inserting a 's'.

Input:   str1 = "cat", str2 = "cut"
Output:  1
We can convert str1 into str2 by replacing 'a' with 'u'.

Input:   str1 = "sunday", str2 = "saturday"
Output:  3
Last three and first characters are same.  We basically
need to convert "un" to "atur".  This can be done using
below three operations. 
Replace 'n' with 'r', insert t, insert a
"""
#Recursive - O(3^n)
def distance(word1,word2,i,j):
    if i == 0:
        return j
    elif j == 0:
        return i 
    elif word1[i] == word2[j]:
        return distance(word1,word2,i-1,j-1)
    else:
        return 1+min(distance(word1,word2,i,j-1), #insert
                    distance(word1,word2,i-1,j), #remove
                    distance(word1,word2,i-1,j-1)) #replace

#DP - Tablulization - O(m*n)
def distance2(word1,word2):
    m = len(word1)+1
    n = len(word2)+1
    table = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif word1[i-1] == word2[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1+min(table[i][j-1], table[i-1][j], table[i-1][j-1])
    print(table)
    return table[m-1][n-1]

# Memoization - O(m*n) time and O(m*n) space
def distance3(word1,word2,i,j,table):
    if i == 0:
        return j
    elif j == 0:
        return i
    elif table[i-1][j-1] != -1:
        return table[i-1][j-1]  
    elif word1[i-1] == word2[j-1]:
        table[i-1][j-1] = distance3(word1,word2,i-1,j-1,table)
        return table[i-1][j-1]
    else:
        table[i-1][j-1] = 1+min(distance3(word1,word2,i,j-1,table), #insert
                    distance3(word1,word2,i-1,j,table), #remove
                    distance3(word1,word2,i-1,j-1,table)) #replace
        return table[i-1][j-1]


#DP - Tablulization - O(m*n) and less space
def distance4(word1,word2):
    m = len(word1)
    n = len(word2)
    table = [[0 for _ in range(n)] for _ in range(2)]
    for i in range(m):
        for j in range(n):
            if i == 0:
                table[i][j] = j
            if j == 0:
                table[i%2][j] = i
            elif word1[i-1] == word2[j-1]:
                table[i%2][j] = table[(i-1)%2][j-1]
            else:
                table[i%2][j] = 1+min(table[i%2][j-1], table[(i-1)%2][j], table[(i-1)%2][j-1])
    print(table)
    return table[(m-1)%2][n-1]

if __name__ == "__main__":
    word1,word2 =["sunday","saturday"] 
    # word1,word2 = [ "mond","monday"]
    # word1,word2 =["cat","cut"]
    # word1,word2 =["geek", "gesek"]

    # output = distance(word1,word2,len(word1)-1,len(word2)-1)
    output = distance2(word1,word2)
    print(output)
    # i = len(word1)
    # j = len(word2)
    # table = [[-1 for _ in range(j)] for _ in range(i)]
    # output = distance3(word1,word2,i,j,table)
    output = distance4(word1,word2)
    print(output)
    # print(table)