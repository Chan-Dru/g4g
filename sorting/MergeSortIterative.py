def merge(L,R):
    if(not len(L) or not len(R)):
        return L or R
    new_arr = []
    i=j=0
    while(len(new_arr)<len(L)+len(R)):
        if(L[i]<R[j]):
            new_arr.append(L[i])
            i += 1
        else:
            new_arr.append(R[j])
            j += 1
        if(len(L)==i or len(R)==j):
            new_arr.extend(L[i:] or R[j:])
            break
    return new_arr

def MergeSortIterative(arr):
    n = len(arr)
    if(n<2):
        return arr
    mid = n//2
    L = MergeSortIterative(arr[:mid])
    R = MergeSortIterative(arr[mid:])
    return merge(L,R)


if __name__ == "__main__":
    arr = [5,7,2,8,1,9,6]
    print(arr)
    print("sorted array is {}".format(MergeSortIterative(arr)))
