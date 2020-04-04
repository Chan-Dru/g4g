def StoogeSort(arr,low,high):
    if low>=high:
        return 
    if(arr[low]>arr[high]):
        arr[low],arr[high] = arr[high],arr[low]
    if high-low+1>2:
        l = (high-low+1)//3
        StoogeSort(arr,low,high-l)
        StoogeSort(arr,low+l,high)
        StoogeSort(arr,low,high-l)

if __name__ == "__main__":
    arr = [6,2,3,8,5,5,4,1,9,5,0]
    print(arr)
    StoogeSort(arr,0,len(arr)-1)
    print("Sorted array is {}".format(arr))