def MergeSort(arr):
    n = len(arr)
    if(n>1):
        mid = n//2
        L = arr[:mid]
        R = arr[mid:]
        MergeSort(L)
        MergeSort(R)
        i=j=k = 0
        while(i < len(L) and j < len(R)):
            if(L[i]<R[j]):
                arr[k]=L[i]
                i += 1
            elif(R[j]<L[i]):
                arr[k]=R[j]
                j += 1
            k += 1
        while(i< len(L)):
            arr[k] = L[i]
            k += 1
            i += 1
        while(j< len(R)):
            arr[k] = R[j]
            k += 1
            j += 1

if __name__ == "__main__":
    arr = [5,7,2,8,1,9,6]
    print(arr)
    MergeSort(arr)
    print("sorted array is {}".format(arr))
