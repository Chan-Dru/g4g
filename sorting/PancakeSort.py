def flip(arr,cur):
    for i in range((cur+1)//2):
        arr[i],arr[cur-i]=arr[cur-i],arr[i]
    # print(arr,cur)

def PancakeSort(arr):
    n = len(arr)
    for j in range(n-1):
        max_cur = 0
        for i in range(n-j):
            if arr[i]>max_cur:
                max_cur = arr[i]
                cur = i
        # print(cur,n-j-1)
        if cur != n-j-1:
            flip(arr,cur)
            flip(arr,n-j-1)

if __name__ == "__main__":
    arr = [8,4,1,3,7,2,9,5,6,0]
    print(arr)
    PancakeSort(arr)
    print("Sorted array is {}".format(arr))