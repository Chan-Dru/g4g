"""
Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True  
There is a subset (4, 5) with sum 9.

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 30
Output: False
There is no subset that add up to 30.
"""
# Recursion
def dp(arr,n,s):
    if n>=0:
        if s > 0:
            return dp(arr,n-1,s)|dp(arr,n-1,s-arr[n-1])
        elif s == 0:
            return True
    return False

# Memoization
def dp1(arr,n,s,table):
    if n>=0 and s>=0:
        if table[n][s] != -1:
            return table[n][s]
        elif s > 0:
            table[n][s] = dp1(arr,n-1,s,table) | dp1(arr,n-1,s-arr[n-1],table)
            return table[n][s]
        elif s == 0:
            return True
    return False

# Tabulation
def dp2(arr,n,s):
    table = [[False for _ in range(s+1)] for _ in range(n+1)]
    for i in range(n+1):
        table[i][0] = True
    for i in range(1,n+1):
        for j in range(1,s+1):
            if j >= arr[i-1]:
                table[i][j] = table[i-1][j] | table[i-1][j-arr[i-1]]
            else:
                table[i][j] = table[i-1][j]
    print(table)
    return table[n][s]


    

if __name__ == "__main__":
    arr = [3, 34, 4, 12, 5, 2]
    arr =[3,4,5,2]
    n = len(arr)
    s = 10
    s = 6
    print("Recurrsion")
    output = dp(arr,n,s)
    print(output)
    print("Memoization")
    table = [[-1 for _ in range(s+1)] for _ in range(n+1)]
    output = dp1(arr,n,s,table)
    print(table)
    print(output)
    print("Tabulation")
    output = dp2(arr,n,s)
    print(output)
    
