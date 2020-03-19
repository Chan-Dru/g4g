def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_n = i
        for j in range(i+1,n):
            if(arr[j] < arr[min_n]):
                min_n = j
        if (min_n != i):
            arr[i],arr[min_n]=arr[min_n],arr[i]
            # swap in python
            # temp = arr[i]
            # arr[i] = arr[min_n]
            # arr[min_n] = temp
    return arr

if __name__=="__main__":
    arr = [30,25,35,20,15,27,10]
    sort_arr = SelectionSort(arr)
    print("Sorted array of {} is {}".format(arr,sort_arr))