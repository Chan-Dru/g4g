def ShellSort(arr):
    n = len(arr)
    shell = n//2 # if shell = 1 it is pure insertion sort
    count = 0
    while(shell > 0):
        for i in range(shell,n):
            j = i - shell
            key = arr[i]
            while(j >= 0 and arr[j]>key):
                arr[j+shell] = arr[j]
                j -= shell
            arr[j+shell] = key
        shell //= 2


if __name__ == "__main__":
    arr = [5,7,2,8,1,9,6]
    print(arr)
    ShellSort(arr)
    print("Sorted array is {}".format(arr))