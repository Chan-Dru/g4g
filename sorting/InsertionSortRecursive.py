def InsertionSortRecursive(arr,n):
    if n <= 1:
        return
    InsertionSortRecursive(arr,n-1)
    key = arr[n-1]
    j=n -2
    while(j>=0 and arr[j]>key):
        arr[j+1] = arr[j]
        j = j - 1
    arr[j+1] = key

if __name__ == "__main__":
    arr = [5,7,2,8,1,9,6]
    print(arr)
    InsertionSortRecursive(arr,len(arr))
    print("sorted array is {}".format(arr))