def partition(arr,l,h):
    pivot = arr[h]
    i = l-1
    j = l
    while (j<h):
        if(arr[j]<pivot):
            i += 1
            arr[i],arr[j] = arr[j],arr[i]
        j += 1
    i += 1
    arr[i],arr[h]=arr[h],arr[i]
    return i

def QuickSort(arr,l,h):
    if(l<h):
        p = partition(arr,l,h)
        print(p,arr[p])
        QuickSort(arr,l,p-1)
        QuickSort(arr,p+1,h)

if __name__ == "__main__":
    arr = [1,5,3,7,2,8,6,9]
    print(arr)
    l = 0
    h = len(arr)-1
    QuickSort(arr,l,h)
    print("Sorted array is {}".format(arr))