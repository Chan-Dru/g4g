"""
LCS for input Sequences “ABCDGH” and “AEDFHR” is “ADH” of length 3.
LCS for input Sequences “AGGTAB” and “GXTXAYB” is “GTAB” of length 4.
"""

def LCS(word1, word2):
    count = [0]*26
    for c in word1:
        count[ord(c)-65] += 1
    output = ""
    for c in word2:
        if count[ord(c)-65] != 0:
            count[ord(c)-65] -= 1
            output += c
    return output

#tabulation
def LCS_DP(word1, word2):
    n = len(word1)
    m = len(word2)
    table = [[0 for i in range(m+1)] for j in range(n+1)]

    for i in range(n+1):
        for j in range(m+1):
            if i ==0 or j == 0:
                table[i][j] = 0
            elif word1[i-1] == word2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    index = table[i][j]
    out = ""
    i = n
    j = m
    while i >0 and j >0:
        if word1[i-1] == word2[j-1]:
            out = word1[i-1]+out
            i -=1
            j -=1
        elif table[i-1][j] > table[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    return out

# memoization
def lcs(word1, word2, n, m, table):
    if n ==0 or m==0:
        return 0
    elif table[n-1][m-1] != 0:
        return table[n-1][m-1]
    elif word1[n-1] == word2[m-1]:
        table[n-1][m-1] = 1 + lcs(word1, word2, n-1, m-1, table)
    else:
        table[n-1][m-1] = max(lcs(word1,word2,n-1,m,table) , lcs(word1,word2,n,m-1,table))
    return table[n-1][m-1]

if __name__ == "__main__":
    word1 = "AGGTAB"
    word2 = "GXTXAYB"
    # lcs = LCS(word1,word2)
    # lcs = LCS_DP(word1,word2)
    # print("LCS for input Sequences {} and {} is {} of lenght {}".format(word1,word2,lcs,len(lcs)))
    
    n = len(word1)
    m = len(word2)
    table = [[0 for i in range(m)] for j in range(n)]
    lcs = lcs(word1,word2,n,m,table)
    # print(table)
    print(lcs)
    i = n
    j = m
    out = ""
    while i >= 0 or j >= 0:
        if word1[i-1] == word2[j-1]:
            out = word1[i-1]+out
            i -= 1
            j -= 1
        elif table[i][j] == table[i-1][j]:
            i -= 1
        else:
            j -= 1
    print(out)