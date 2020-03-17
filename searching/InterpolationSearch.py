def InterpolationSearch(arr,key,l,h):
    while(l<=h and key <= arr[h] and key >= arr[l]):
        pos = l + int((h-l)/(arr[h]-arr[l])*(key-arr[l]))
        print(l,h,pos,arr[pos])
        if arr[pos] == key:
            return pos
        elif arr[pos] < key:
            l = pos +1
        else:
            h = pos-1
    return -1

if __name__ == "__main__":
    arr = [1,4,7,10,15,40,41,42,43,44,45,46,55,60,100]
    key = 60
    l = 0
    h = len(arr)-1
    index = InterpolationSearch(arr,key,l,h)
    if(index <0):
        print("key {} is not found in arr".format(key))
    else:
        print("key {} is found in the index {}".format(key,index))