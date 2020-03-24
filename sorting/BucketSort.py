def InsertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i -1
        while(j >= 0 and arr[j]>key):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr

def BucketSort(arr):
    n = len(arr)
    bucket = dict()
    output = []
    for i in range(n):
        bucket[i] = []
    for i in arr:
        bucket[int(i*n)].append(i)
    for i in range(n):
        bucket[i] = InsertionSort(bucket[i])
    for i in range(n):
        output.extend(bucket[i])
    return output

if __name__ == "__main__":
    arr = [0.897, 0.565, 0.1234, 0.665, 0.656, 0.3434]
    print(arr)
    output = BucketSort(arr)
    print("Sorted array is {}".format(output))