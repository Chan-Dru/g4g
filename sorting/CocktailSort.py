def CocktailSort(arr):
    n = len(arr)
    swapped = True
    j = 1
    while(swapped):
        swapped = False
        for i in range(j-1,n-j):
            if(arr[i]>arr[i+1]):
                arr[i],arr[i+1]=arr[i+1],arr[i]
                swapped = True
        # print(arr)
        for i in range(n-j-1,j-1,-1):
            if(arr[i]<arr[i-1]):
                arr[i],arr[i-1]=arr[i-1],arr[i]
                swapped=True
        # print(arr)
        j+=1

if __name__ == "__main__":
    arr = [5,8,2,4,9,0,1,7,3,6]
    print(arr)
    CocktailSort(arr)
    print("Sorted array is {}".format(arr))