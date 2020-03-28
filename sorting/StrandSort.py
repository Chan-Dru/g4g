def merge(subarray,output):
    n1 = len(subarray)
    n2 = len(output)
    n = n1+n2
    temp = [0]*n
    i=j=k=0
    while(i<n1 and j<n2):
        if(subarray[i]<=output[j]):
            temp[k] = subarray[i]
            i += 1
        else:
            temp[k] = output[j]
            j += 1
        k += 1
    while(i<n1):
        temp[k] = subarray[i]
        i += 1
        k += 1
    while(j<n2):
        temp[k] = output[j]
        j += 1
        k += 1
    return temp


def StrandSort(arr):
    n = len(arr)
    output = []
    while(n>0):
        subarray = []
        key = arr[0]
        for i in range(n):
            if(arr[i]>=key):
                key = arr[i]
                subarray.append(arr[i])
        for i in subarray:
            arr.remove(i)
        # print(arr,subarray)
        output = merge(subarray,output)
        # print(output)
        n=len(arr)
    return output
if __name__ == "__main__":
    arr = [3,7,5,1,8,2,2,3,4,9,0,4]
    print(arr)
    output = StrandSort(arr)
    print("Sorted array is {}".format(output))