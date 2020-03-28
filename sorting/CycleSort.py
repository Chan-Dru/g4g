def CycleSort(arr):
    n = len(arr)
    writes = 0
    for cyclestart in range(n-1):
        pos = cyclestart
        key = arr[pos]
        for i in range(cyclestart+1,n):
            if arr[i]<key:
                pos+=1
        if(pos==cyclestart):
            continue
        while(arr[pos]==key):
            pos+=1
        arr[pos],key = key,arr[pos]
        writes+=1
        # print(writes,cyclestart,arr, key)
        
        while(pos!=cyclestart):
            pos = cyclestart
            for i in range(cyclestart+1,n):
                if arr[i]<key:
                    pos+=1
            while(arr[pos]==key):
                pos+=1
            arr[pos],key = key,arr[pos]
            writes += 1
            # print(writes,cyclestart,arr,key)


if __name__ == "__main__":
    arr = [5,5,5,2,8,6,1,9,4,3]
    print(arr)
    CycleSort(arr)
    print("Sorted array is {}".format(arr))