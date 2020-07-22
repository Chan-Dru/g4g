"""
ab: Number of insertions required is 1 i.e. bab
aa: Number of insertions required is 0 i.e. aa
abcd: Number of insertions required is 3 i.e. dcbabcd
abcda: Number of insertions required is 2 i.e. adcbcda which is same as number of insertions in the substring bcd(Why?).
abcde: Number of insertions required is 4 i.e. edcbabcde
"""
# recursion
def dp(word,i,j):
    if i<=j:
        if word[i] == word[j]:
            return dp(word,i+1,j-1)
        else:
            return 1+min(dp(word,i+1,j),dp(word,i,j-1))
    return 0

# memoization
def dp1(word,i,j,table):
    if i<=j:
        if table[i][j] != -1:
            # print(i,j)
            return table[i][j]
        elif word[i] == word[j]:
            table[i][j] = dp1(word,i+1,j-1,table)
            return table[i][j]
        else:
            table[i][j] = 1+min(dp1(word,i+1,j,table), dp1(word,i,j-1,table))
            return table[i][j]
    return 0

# tabulation
def dp2(word):
    table = [[0 for _ in range(n)] for _ in range(n)]
    for g in range(1,n):
        for j in range(g,n):
            i = j-g
            if word[i] == word[j]:
                table[i][j] = table[i+1][j-1]
            else:
                table[i][j] = 1+min(table[i+1][j],table[i][j-1])
    print(table)
    return table[0][n-1]

if __name__ == "__main__":
    word = "abcde"
    n = len(word)
    print("recursion")
    output = dp(word,0,n-1)
    print(output)
    print("memoization")
    table = [[-1 for _ in range(n)] for _ in range(n)]
    output = dp1(word,0,n-1,table)
    print(table)
    print(output)
    print("tabulation")
    output = dp2(word)
    print(output)