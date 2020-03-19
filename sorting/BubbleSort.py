def BubbleSort(arr):
    n = len(arr)
    flag = True
    j = 0
    while(flag == True):
        j = j +1
        flag = False
        for i in range(n-j):
            if arr[i]>arr[i+1]:
                arr[i+1],arr[i]=arr[i],arr[i+1]
                flag = True
    return arr


if __name__=="__main__":
    # arr = [30,25,35,20,15,27,10]
    arr = [9,1,2,3,4,5,6,7,8]
    print(arr)
    BubbleSort(arr)
    print("Sorted array is {}".format(arr))