from threading import Timer
from time import sleep

def SleepSort(arr):
    SleepSort.result = []
    def add1(x):
        SleepSort.result.append(x)
    mx = arr[0]
    for v in arr:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return SleepSort.result

if __name__ == "__main__":
    arr = [6,2,3,8,4,1,9,5,0]
    print(arr)
    arr = SleepSort(arr)
    print("Sorted array is {}".format(arr))