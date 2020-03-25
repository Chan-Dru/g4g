import random
RUN = 20
def InsertionSort(arr,left,right):
    for i in range(left+1,right+1):
        j = i-1
        key = arr[i]
        while(j>=left and arr[j]>key):
            arr[j+1]=arr[j]
            j = j-1
        arr[j+1]=key

def merge(arr,left,mid,right):
    n1 = mid-left+1
    n2 = right-mid
    L1 = []
    L2 = []
    print(n1,n2,left,mid,right)
    for i in range(n1):
        L1.append(arr[left+i])
    for i in range(n2):
        L2.append(arr[mid+i+1])
    i=j =0
    k = left
    while(i<n1 and j<n2):
        if(L1[i]<=L2[j]):
            arr[k]=L1[i]
            i+=1
        else:
            arr[k]=L2[j]
            j+=1
        k+=1
    while(i<n1):
        arr[k]=L1[i]
        i+=1
        k+=1
    while(j<n2):
        arr[k]=L2[j]
        j+=1
        k+=1

def TimSort(arr , n):
    for i in range(0,n,RUN):
        InsertionSort(arr,i,min(i+RUN-1,n-1))
    size = RUN
    while(size<n):
        for left in range(0,n,2*size):
            mid = min(left + size -1, n-1)
            right = min(mid + size -1, n-1)
            merge(arr,left,mid,right)
        size = 2*size

if __name__ == "__main__":
    # arr = [1,6,3,8,4,9,2,5,8]
    arr = list(range(100))
    random.shuffle(arr)
    arr = [22, 76, 86, 15, 87, 14, 55, 36, 61, 60, 28, 10, 84, 5, 37, 68, 57, 27, 70, 2, 91, 72, 9, 31, 42, 56, 82, 13, 39, 35, 90, 20, 4, 63, 67, 30, 44, 47, 29, 58, 1, 52, 0, 6, \
            43, 19, 46, 79, 85, 26, 25, 48, 80, 77, 78, 18, 99, 11, 73, 59, 23, 62, 96, 16, 53, 71, 75, 98, 8, 65, 17, 21, 41, 83, 32, 49, 40, 54, 95, 3, 93, 12, 66, 94, 92, 64, 50, \
            38, 7, 81, 74, 24, 51, 88, 69, 45, 34, 33, 97, 89]
    print(arr)
    n = len(arr)
    TimSort(arr,n)
    print("Sorted array is {}".format(arr))