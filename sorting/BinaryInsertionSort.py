def BinarySearch(arr,key,low,high):
    if low == high:
        if arr[low]>key:
            return low
        else:
            return low+1
    if low > high:
        return low

    if low<high:
        mid = low+(high-low)//2
        if arr[mid]==key:
            return mid
        if arr[mid] > key:
            high = mid-1
        if arr[mid] < key:
            low = mid + 1
        return BinarySearch(arr,key,low,high)


def BinaryInsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        k = arr[i]
        j = BinarySearch(arr,k,0,i-1)
        arr = arr[:j]+[k]+arr[j:i]+arr[i+1:]
    return arr


if __name__ == "__main__":
    arr = [6,2,3,8,4,1,9,5,0]
    print(arr)
    arr = BinaryInsertionSort(arr)
    print("Sorted array is {}".format(arr))