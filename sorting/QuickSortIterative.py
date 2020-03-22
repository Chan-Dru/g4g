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

def QuickSort(arr):
    n = len(arr)-1
    stack = [0]*n
    top = -1

    top += 1
    stack[top] = 0
    top += 1
    stack[top] = n
    while(top >= 0):
        h = stack[top]
        top -= 1
        l = stack[top]
        top -= 1
        p = partition(arr,l,h)
        if(l<p-1):
            top += 1
            stack[top] = l
            top += 1
            stack[top] = p-1
        if(p+1<h):
            top += 1
            stack[top] = p+1
            top += 1
            stack[top] = h


if __name__ == "__main__":
    arr = [1,5,3,7,2,8,6,9]
    print(arr)
    l = 0
    h = len(arr)-1
    QuickSort(arr)
    print("Sorted array is {}".format(arr))