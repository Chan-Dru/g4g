"""
Ugly numbers are numbers whose only prime factors are 2, 3 or 5.
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. 
By convention, 1 is included.

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
"""

import time
# Traversing all number and finding it is ugly till the nth ugly number is found

ugly_numbers = []

def maxdivide(a,b):
    while(b%a == 0):
        b = b/a
        if b in ugly_numbers:
            return 1
    # print(b,a)
    return b

def isugly(n):
    n = maxdivide(2,n)
    n = maxdivide(3,n)
    n = maxdivide(5,n)
    return n==1

def ugly(n):
    i = 1
    # ugly_no = 1
    prime_no = [2,3,5]
    pt = 1
    while(i <= n):
        if isugly(pt):
            # print(pt)
            ugly_numbers.append(pt)
            ugly_no = pt
            i += 1
        pt += 1
    # return ugly_numbers[-1]
    return ugly_no

def ugly_DP(n):
    ugly = [1]
    i = 0
    i2 = i3 = i5 = 0
    mul_2 = ugly[i2]*2
    mul_3 = ugly[i3]*3
    mul_5 = ugly[i5]*5
    while(i < n-1):
        next_ugly = min(mul_2, mul_3, mul_5)
        ugly.append(next_ugly)
        i += 1
        if next_ugly == mul_2:
            i2 += 1
            mul_2 = ugly[i2]*2
        if next_ugly == mul_3:
            i3 += 1
            mul_3 = ugly[i3]*3
        if next_ugly == mul_5:
            i5 += 1
            mul_5 = ugly[i5]*5
    # print(ugly)
    return ugly[-1]

if __name__ == '__main__':
    import timeit
    t1 = time.time()
    print(ugly_DP(1000))
    # print(ugly(1000))
    t2 = time.time()
    print(t2-t1,t2,t1)
    # print(timeit.timeit("ugly(150)", setup="from __main__ import ugly"))

