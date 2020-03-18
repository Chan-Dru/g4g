def BinarySearch(arr,l,h,key):
    if(l<=h):
        mid = l + (h-l)//2
        if(arr[mid]==key):
            return mid
        elif(arr[mid]<key):
            l = mid+1
        else:
            h = mid-1
        return BinarySearch(arr,l,h,key)
    return -1


def ExponentialSearch(arr,key):
    range = 1
    n=len(arr)
    while(range<=n and arr[range]<key):
        range = range*2
    l = range//2
    h = min(range,n)
    return BinarySearch(arr,l,h,key)

if __name__ == "__main__":
    arr = [1,3,5,7,9,11,13,15,17,19]
    key = 19
    index = ExponentialSearch(arr,key)
    if index <0:
        print("key {} is not found".format(key))
    else:
        print("key {} is found at the index {}".format(key,index))