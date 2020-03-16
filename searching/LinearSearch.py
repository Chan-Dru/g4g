def LinearSearch(arr,key):
    n = len(arr)
    for i in range(n):
        if arr[i]==key:
            return i
    return -1


if __name__=="__main__":
    a = [1,4,5,8,11,25,3]
    key = 20
    index = LinearSearch(a,key)
    if index > 0:
        print("key {0} is found at index {1}".format(key,index))
    else:
        print("key {0} is not found in array".format(key))