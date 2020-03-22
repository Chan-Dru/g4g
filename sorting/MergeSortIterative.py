def mergeSort(arr):
    currentsize = 1
    n = len(arr)-1
    while(currentsize < n):
        left = 0
        # print(currentsize,left)
        while(left < n):
            mid = left + currentsize -1
            right = (currentsize *2 + left -1,n)[currentsize *2 + left -1   >n]
            # print(currentsize,left,mid,right)
            merge(arr,left,mid,right)
            # print(arr)
            left = left + currentsize*2
        currentsize = currentsize * 2

def merge(arr,left,mid,right):
    n1 = mid - left +1
    n2 = right - mid
    L1 = [0]*n1
    L2 = [0]*n2
    for i in range(n1):
        L1[i] = arr[left+i]
    for i in range(n2):
        L2[i] = arr[mid+i+1]
    # print(L1,L2)
    i = j = 0
    k = left
    while(i<n1 and j <n2):
        if(L1[i]<L2[j]):
            arr[k] = L1[i]
            i += 1
        else:
            arr[k] = L2[j]
            j += 1
        k += 1
    while(i < n1):
        arr[k] = L1[i]
        i += 1
        k += 1
    while(j < n2):
        arr[k] = L2[j]
        j += 1
        k += 1


if __name__ == "__main__":
    arr = [5,7,2,8,1,9,6]
    print(arr)
    mergeSort(arr)
    print("sorted array is {}".format(arr))
