import math

def JumpSearch(arr, n, key, jump):
    i = 0
    while(i < n and arr[i]<key):
        i = i + jump
    if i == 0:
        return -1
    else:
        j=i-jump
        while(j<n and j<i):
            if(arr[j]==key):
                return j
            j = j + 1
    return -1
if __name__ == "__main__":
    arr = range(50)
    key = 22
    n = len(arr)
    jump = int(math.sqrt(n))
    index = JumpSearch(arr,n,key,jump)
    if index > -1:
        print("key {} is found at index {}".format(key,index))
    else:
        print("key {} is not found".format(key))