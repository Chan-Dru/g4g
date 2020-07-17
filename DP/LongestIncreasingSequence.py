"""
Input: arr[] = {3, 10, 2, 1, 20}
Output: Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input: arr[] = {3, 2}
Output: Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input: arr[] = {50, 3, 10, 7, 40, 80}
Output: Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
"""
# Dynamic Programming
def DP(array):
    n = len(array)
    DP = [1]*n
    prev = [-1]*n
    maxLength = 1
    bestEnd = 0
    # Finding the length of longest subsequence
    for i in range(1,n):
        for j in range(i,-1,-1):
            if (DP[j] + 1 > DP[i] and array[j] < array[i]):
                DP[i] = DP[j] + 1
                prev[i] = j
        if (DP[i] > maxLength):
            bestEnd = i
            maxLength = DP[i]

    print(maxLength,bestEnd,DP,prev)
    # Framing the Longest subsequence using bestEnd and prev array
    out = []
    while(bestEnd != -1):
        out.append(array[bestEnd])
        bestEnd = prev[bestEnd]
    print(out)
    print("The longest increasing subsequence is {}".format(out[::-1]))


def ceilBinarySearch(array,endElement,key,low,high):
    if high > low:
        mid = low + (high-low)//2
        if array[endElement[mid]] < key:
            low = mid +1
        else:
            high = mid
        return ceilBinarySearch(array,endElement,key,low,high)
    else:
        # print(low,high)
        return high


# O(nLogn) using BinarySearch
def LIS(array):
    n = len(array)

    endElement = []
    parent = [-1]*n
    
    if n > 0:
        endElement.append(0)
    
    for i in range(1,n):
        element = array[i]
        pos = len(endElement)
        if element > array[endElement[pos-1]]:
            parent[i]=endElement[pos-1]
            endElement.append(i)
        else:
            pos = ceilBinarySearch(array,endElement,element,0,pos)
            endElement[pos] = i
            if pos !=0:
                parent[i] = endElement[pos-1]
        # print(endElement)
        # print(parent)
    print(endElement, parent)
    out =[]
    bestEnd = endElement[-1]
    while bestEnd != -1:
        out.append(array[bestEnd])
        bestEnd = parent[bestEnd]
    print(out)
    print("The longest increasing subsequence is {}".format(out[::-1]))

array = [50,10, 22, 9, 33, 21, 50, 41, 60 ] 
print(array)

t1 = LIS(array)
t = DP(array)