"""
Input:   str1 = "geek",  str2 = "eke"
Output: "geeke"

Input:   str1 = "AGGTAB",  str2 = "GXTXAYB"
Output:  "AGXGTXAYB"
"""
# Recursion
def dp(word1,word2,i,j,n,m):
    if i>n:
        return word2[j:]
    if j>m:
        return word1[i:] 
    if word1[i] == word2[j]:
        return word1[i]+dp(word1,word2,i+1,j+1,n,m)
    else:
        l = word1[i]+dp(word1,word2,i+1,j,n,m)
        r = word2[j]+dp(word1,word2,i,j+1,n,m)
        if len(l) < len(r):
            return l
        else:
            return r

# Memoization
def dp1(word1,word2,i,j,n,m,table):
    if i>n:
        return word2[j:]
    if j>m:
        return word1[i:] 
    if table[i][j] != -1:
        return table[i][j]
    if word1[i] == word2[j]:
        return word1[i]+dp1(word1,word2,i+1,j+1,n,m,table)
    else:
        l = word1[i]+dp1(word1,word2,i+1,j,n,m,table)
        r = word2[j]+dp1(word1,word2,i,j+1,n,m,table)
        if len(l) < len(r):
            table[i][j] = l
            return l
        else:
            table[i][j] = r
            return r

# Tabulation
def dp2(word1,word2):
    n = len(word1)
    m = len(word2)
    table = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
       table[i][0] = i
    for i in range(m+1):
        table[0][i] = i

    for i in range(1,n+1):
        for j in range(1,m+1):
            if word1[i-1] == word2[j-1]:
                table[i][j] = table[i-1][j-1]+1
            else:
                table[i][j] = 1+min(table[i-1][j], table[i][j-1])
    print(table)
    output = ""
    i = n
    j = m
    while(i>0 and j>0):
        if word1[i-1] == word2[j-1]:
            output = word1[i-1]+output
            i -= 1
            j -= 1
        else:
            if table[i-1][j] > table[i][j-1]:
                output = word2[j-1]+output
                j -= 1
            else:
                output = word1[i-1]+output
                i -= 1
    if i==0:
        while(j>0):
            output = word2[j-1]+output
            j -= 1
    if j==0:
        while(i>0):
            output = word1[i-1]+output
            i -= 1
    return output

if __name__ == "__main__":
    word1 = "AGGTAB"
    # word2 = "AGGTABM"
    word2 = "GXTXAYB"
    n = len(word1)-1
    m = len(word2)-1
    i =j = 0
    print("Recurrsion")
    output = dp(word1,word2,i,j,n,m)
    print(output)
    print("Memoization")
    table = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    output = dp1(word1,word2,i,j,n,m,table)
    print(table)
    print(output)
    print("Tabulation")
    output = dp2(word1,word2)
    print(output)