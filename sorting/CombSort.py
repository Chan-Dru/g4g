def CombSort(arr):
    n = len(arr)
    gap = n
    swapped = True
    while(gap != 1 or swapped == True):
        gap = (gap*10//13,1)[gap*10//13 < 1]
        # print(gap)
        swapped = False
        for i in range(0,n-gap):
            if(arr[i] > arr[i+gap]):
                arr[i],arr[i+gap] = arr[i+gap],arr[i]
                swapped = True
        # print(arr)

if __name__ == "__main__":
    arr = [1,6,2,9,3,7,4,0,5]
    print(arr)
    CombSort(arr)
    print("Sorted array is {}".format(arr))