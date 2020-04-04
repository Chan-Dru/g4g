import random

def Shuffle(arr,n):
    for i in range(n):
        r = random.randint(0,n-1)
        arr[i],arr[r]=arr[r],arr[i]

def IsSorted(arr,n):
    for i in range(0,n-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def BogoSort(arr):
    n = len(arr)
    while not IsSorted(arr,n):
        Shuffle(arr,n)

if __name__ == "__main__":
    arr = [6,2,3,8,4,1,9,5,0]
    print(arr)
    BogoSort(arr)
    print("Sorted array is {}".format(arr))