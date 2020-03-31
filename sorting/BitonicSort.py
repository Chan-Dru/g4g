def compAndSwap(arr,low,high,flag):
    if (flag == 1 and arr[low]>arr[high]) or (flag == 0 and arr[low]<arr[high]):
        arr[low],arr[high]=arr[high],arr[low]

def BitonicMerge(arr,low,high,flag):
    if high>1:
        k = high//2
        for i in range(low,low+k):
            compAndSwap(arr,i,i+k,flag)
        BitonicMerge(arr,low,k,flag)
        BitonicMerge(arr,low+k,k,flag)

def BitonicSort(arr,low,high,flag):
    if high>1:
        k = high//2
        BitonicSort(arr,low,k,1)
        BitonicSort(arr,low+k,k,0)
        BitonicMerge(arr,low,high,flag)

if __name__ == "__main__":
    arr = [7,2,1,3,8,5,9,4,0,6]
    print(arr)
    n = len(arr)
    # works if length of array is in multiple of 8 , if not pad the array to make it
    pad = 8-n%8
    temp = [-1]*pad
    arr = temp + arr

    BitonicSort(arr,0,len(arr),1)
    print("Sorted array is {}".format(arr[pad:]))