"""
Imagine you have a special keyboard with the following keys: 
Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it
                 after what has already been printed. 

If you can only press the keyboard for N times (with the above four
keys), write a program to produce maximum numbers of A's. That is to
say, the input parameter is N (No. of keys that you can press), the 
output is M (No. of As that you can produce).
"""

def maxA1(n):
    if n < 0:
        return -1
    if n < 7:
        return n
    maxi = 0
    for i in range(n-3,0,-1):
        cur = (n-i-1)*maxA1(i)
        # print(i,cur)
        if cur > maxi:
            maxi = cur
    return maxi

n = 20
print(maxA1(n))

def maxA2(n):
    best = [0]*(n+1)
    for i in range(1,n+1):
        best[i] = best[i-1]+1
        print("=====>",i,best[i])
        for j in range(2,i-3):
            best[i] = max(best[i], best[j] + best[j]*(i-j-2))
            print(j,i-j-1,best[j],best[i])

    return best[n]


# n = 11
# print(maxA2(n))

def maxA3(n):
    if n < 7:
        return n
    best = [0]*(n+1)
    for i in range(7):
        best[i] = i

    for i in range(7,n+1):
        best[i] = max(2*best[i-3], max(3*best[i-4],4*best[i-5]))

    return best[i]

# n = 7
# print(maxA3(n))

def maxA4(n):
    best = [0, 1, 2, 3, 4, 5, 6, 9, 12, 16, 20, 27, 36, 48, 64, 81]
    if n < 16:
        return best[n]
    q = (n-11)//5
    return (best[n-5*q])*(4**q)

n = 20
print(maxA4(n))
