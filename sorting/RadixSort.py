def CountingSort(arr,exp):
    n = len(arr)
    count = [0]*10
    for i in arr:
        index = i//exp
        count[index%10] += 1
    print(count)
    for i in range(1,10):
        count[i] += count[i-1]
    print(count)
    output = [0]*n
    for i in arr[::-1]:
        index = i//exp
        count[index%10] -= 1
        output[count[index%10]] = i
    print(output)
    for i in range(n):
        arr[i] = output[i]

def RadixSort(arr):
    max_ = max(arr)
    expp = 1
    while(max_//expp > 0):
        CountingSort(arr,expp)
        expp *= 10

if __name__ == "__main__":
    arr = [ 170, 45, 75, 90, 802, 24, 2, 66] 
    print(arr)
    RadixSort(arr)
    print("Sorted array is {}".format(arr))