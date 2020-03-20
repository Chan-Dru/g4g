def InsertionSort(arr):
    n = len(arr)
    i = 0
    for i in range(1,n):
        j = i - 1
        key = arr[i]
        while(j>=0 and arr[j]>key):
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
        # if(arr[i]<arr[j]):
        #     k = 0
        #     while(arr[k]<arr[i]):
        #         k = k +1
        #     l = i
        #     t = arr[i]
        #     while(l>k):
        #         arr[l]=arr[l-1]
        #         l = l -1
        #     arr[k] = t
    return arr

if __name__ == "__main__":
    arr = [5,7,2,8,1,9,6]
    print(arr)
    InsertionSort(arr)
    print("sorted array is {}".format(arr))