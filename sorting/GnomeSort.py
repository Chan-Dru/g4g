def GnomeSort(arr):
    n = len(arr)
    t = 1
    forward = 1
    while(t<n):
        if t==0:
            t +=1
        if(arr[t]>arr[t-1]):
            t +=1
        else:
            arr[t],arr[t-1]=arr[t-1],arr[t]
            t -=1


if __name__ == "__main__":
    arr = [6,2,3,8,4,1,9,5,0]
    print(arr)
    GnomeSort(arr)
    print("Sorted array is {}".format(arr))