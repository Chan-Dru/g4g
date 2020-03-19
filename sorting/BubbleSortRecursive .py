def BubbleSortRecursive(arr):
    for i in range(len(arr)-1):
        if(arr[i+1]< arr[i]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
            BubbleSortRecursive(arr)
    return arr


if __name__=="__main__":
    arr = [30,25,35,20,15,27,10]
    # arr = [9,1,2,3,4,5,6,7,8]
    BubbleSortRecursive(arr)
    print("Sorted array is {}".format(arr))