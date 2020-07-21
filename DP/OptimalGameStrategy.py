"""
Pick the first or last element, maximize ur total - User and Oponents take turn, User plays first

5, 3, 7, 10 : The user collects maximum value as 15(10 + 5)
8, 15, 3, 7 : The user collects maximum value as 22(7 + 15)
"""
# def dp(arr,user,opp,n,flag):
#     if n > 0:
#         if flag == True:
#             return max(arr[0]+dp(arr[1:],user+arr[0],opp,n-1,not flag) ,arr[-1]+dp(arr[:-1],user+arr[-1],opp,n-1,not flag))
#         else:
#             return min(dp(arr[1:],user,opp+arr[0],n-1,not flag), dp(arr[:-1],user,opp+arr[-1],n-1,not flag))
#     return 0

def dp(arr,i,j):
    if i < j:
        return max(arr[i]+min(dp(arr,i+2,j),dp(arr,i+1,j-1)), arr[j]+min(dp(arr,i+1,j-1),dp(arr,i,j-2)))
    return 0

# Memoization
def dp1(arr,i,j,table):
    if i<j:
        if table[i][j] != -1:
            return table[i][j]
        else:
            table[i][j] = max(arr[i]+min(dp1(arr,i+2,j,table),dp1(arr,i+1,j-1,table)), arr[j]+min(dp1(arr,i+1,j-1,table),dp1(arr,i,j-2,table)))
            return table[i][j]
    return 0

# Tabulation
def dp2(arr):
    n = len(arr)
    table = [[-1 for _ in range(n)] for _ in range(n)]
    for g in range(n):
        for j in range(g,n):
            i = j-g
            # print(i)
            x = 0
            if i+2 < j:
                x = table[i+2][j]
            y = 0
            if i+1 < j-1:
                y = table[i+1][j-1]
            z = 0
            if i < j-2:
                z = table[i][j-2]
            table[i][j] = max(arr[i]+min(x,y), arr[j]+min(y,z))
    print(table)
    return table[0][n-1]
            

if __name__ == "__main__":
    arr = [ 20, 30, 2, 2, 2, 10]
    n = len(arr)
    # user = opp = 0
    # flag = True # user turn
    # output = dp(arr,user,opp,n,flag)
    # print(output)
    print("Recursion")
    output = dp(arr,0,n-1)
    print(output)
    print("Memoization")
    table = [[-1 for _ in range(n)] for _ in range(n)]
    output = dp1(arr,0,n-1,table)
    print(table)
    print(output)
    print("Tabulation")
    output = dp2(arr)
    print(output)