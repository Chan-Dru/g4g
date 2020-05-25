"""
Input : arr[] = {0, -1, 2, -3, 1}
Output : (0 -1 1), (2 -3 1)

Explanation : The triplets with zero sum are
0 + -1 + 1 = 0 and 2 + -3 + 1 = 0  

Input : arr[] = {1, -2, 1, 0, 5}
Output : 1 -2  1
Explanation : The triplets with zero sum is
1 + -2 + 1 = 0  
"""
arr = [0,-1,2,-3,1]
n = len(arr)
output = []
for i in range(n):
    a = arr[i]
    complement = set()
    for j in range(i+1,n):
        b = -(arr[j] + a)
        if arr[j] in complement:
            output.append([a,b,arr[j]])
        else:
            complement.add(b)
print(output)