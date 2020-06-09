"""
Input: arr[] = {1, 4, 20, 3, 10, 5}, sum = 33
Ouptut: Sum found between indexes 2 and 4
Sum of elements between indices
2 and 4 is 20 + 3 + 10 = 33

Input: arr[] = {1, 4, 0, 0, 3, 10, 5}, sum = 7
Ouptut: Sum found between indexes 1 and 4
Sum of elements between indices
1 and 4 is 4 + 0 + 0 + 3 = 7

Input: arr[] = {1, 4}, sum = 0
Output: No subarray found
There is no subarray with 0 sum
"""

arr = [1, 3, 20, 3, 10, 5]
# arr = [1, 4, 0, 0, 3, 10, 5]
des_sum = 6
fwd_cur = 0
bwd_cur = 0
n = len(arr)
calc_sum = 0

while(fwd_cur < n):
    if calc_sum < des_sum:
        calc_sum += arr[fwd_cur]
        fwd_cur += 1
    else:
        calc_sum -= arr[bwd_cur]
        bwd_cur += 1

    if calc_sum == des_sum:
        print("output",bwd_cur,fwd_cur-1)
        break
