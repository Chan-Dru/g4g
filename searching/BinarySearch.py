def BinarySearch(arr,key,l,h):
    if l < h:
        mid = l+(h-l)//2
        if arr[mid] == key:
            return mid
        elif key < arr[mid]:
            h = mid - 1
        elif key > arr[mid]:
            l = mid + 1
        return BinarySearch(arr,key,l,h)
    else:
        return -1



if __name__ == "__main__":
    a = [1,3,5,7,9,11,13,15,17,19]
    key = 0
    l = 0
    h = len(a)
    index = BinarySearch(a,key,l,h)
    if index >= 0 :
        print("key {} is found at index {}".format(key,index))
    else:
        print("key {} is not found in the array".format(key))