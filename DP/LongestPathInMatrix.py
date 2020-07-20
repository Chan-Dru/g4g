"""
we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacent cells have a difference of 1.
Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9.
"""
# recursion
def dp(mat,m,n,i,j,key):
    if i>=0 and i<m and j>=0 and j<n and mat[i][j] == key+1:
        # print(i,j,mat[i][j],key)
        return 1 + max(dp(mat,m,n,i-1,j,mat[i][j]),dp(mat,m,n,i+1,j,mat[i][j]),dp(mat,m,n,i,j-1,mat[i][j]),dp(mat,m,n,i,j+1,mat[i][j]))
    else:
        return 0

# memoization
def dp1(mat,m,n,i,j,key,table):
    if table[i][j] != -1 and mat[i][j] == key+1:
        return table[i][j]
    if i>=0 and i<m and j>=0 and j<n and mat[i][j] == key+1:
        # print(i,j,mat[i][j],key)
        table[i][j] = 1 + max(dp1(mat,m,n,i-1,j,mat[i][j],table),dp1(mat,m,n,i+1,j,mat[i][j],table),dp1(mat,m,n,i,j-1,mat[i][j],table),dp1(mat,m,n,i,j+1,mat[i][j],table))
        return table[i][j]
    else:
        return 0

if __name__ == "__main__":
    mat =  [[1,2,9],
            [5,3,8],
            [4,6,7]] 
    i = len(mat)
    j = len(mat[0])
    print("Recursion")
    out = 0
    for a in range(i):
        for b in range(j):
            # print("#"*20)
            output = dp(mat,i,j,a,b,mat[a][b]-1)
            # print(output)
            out = max(out,output)
    print(out)

    print("Memoization")
    out = 0
    table = [[-1 for _ in range(j+1)] for _ in range(i+1)]
    for a in range(i):
        for b in range(j):
            if table[a][b] == -1:
                # print("#"*20)
                output = dp1(mat,i,j,a,b,mat[a][b]-1,table)
                # print(output,table)
            out = max(out,table[a][b])
    print(out)
