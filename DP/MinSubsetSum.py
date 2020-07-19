"""
Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 
"""
from collections import defaultdict
# recursive
def dp(arr,set1,i):
    if i >= 0:
        return min(dp(arr,set1+arr[i],i-1) , dp(arr,set1,i-1))
    return abs(set1 - (sum(arr) - set1))

# Memoization
def dp1(arr,set1,i,lookup):
    if i <0:
        return abs(set1 - (sum(arr) - set1))
    key = (i,set1)
    if key not in lookup:
        lookup[key] = min(dp1(arr,set1+arr[i],i-1,lookup) , dp1(arr,set1,i-1,lookup))
    return lookup[key]

# Tabulation
def dp2(arr):
    total = sum(arr)
    n = len(arr)
    table = [[False for _ in range(total+1)] for _ in range(n+1)]
    for i in range(n+1):
        table[i][0] = True
    for i in range(1,n+1):
        for j in range(1,total+1):
            table[i][j] = table[i-1][j]
            if arr[i-1] <= j:
                table[i][j] |= table[i-1][j-arr[i-1]]
    j = total//2
    while(j >= 0 and not table[n][j]):
        j -= 1
    return total-2*j


if __name__ == "__main__":
    arr = [10,20,15,5,25]
    i = len(arr)-1
    set1 =0
    output = dp(arr,set1,i)
    print(output)
    lookup = defaultdict()
    output = dp1(arr,set1,i,lookup)
    print(output)
    output = dp2(arr)
    print(output)
    # print(len(lookup))
    
    