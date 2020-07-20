"""
options : 1, 2 and 3

Input: n = 3
Output: 4
Explantion:
Below are the four ways
 1 step + 1 step + 1 step
 1 step + 2 step
 2 step + 1 step
 3 step

Input: n = 4
Output: 7
Explantion:
Below are the four ways
 1 step + 1 step + 1 step + 1 step
 1 step + 2 step + 1 step
 2 step + 1 step + 1 step 
 1 step + 1 step + 2 step
 2 step + 2 step
 3 step + 1 step
 1 step + 3 step
"""
# recursion
def dp(n):
    if n==0:
        return 1
    elif n>0:
        return dp(n-1) + dp(n-2) + dp(n-3)
    else:
        return 0
         
# Memoization
def dp1(n,table):
    if n == 0:
        return 1
    elif table[n] != -1:
        return table[n]
    elif n>0:
        table[n] = dp1(n-1,table) + dp1(n-2,table) + dp1(n-3,table)
        return table[n]
    else:
        return 0

# Tabulation
def dp2(n):
    table = [1,1,2]
    for i in range(3,n+1):
        table.append(table[i-1]+table[i-2]+table[i-3])
    print(table)
    return table[n]


if __name__ == "__main__":
    n = 4
    output = dp(n)
    print(output)
    table = [-1 for _ in range(n+1)]
    output = dp1(n,table)
    print(output)
    print(table)
    output = dp2(n)
    print(output)
