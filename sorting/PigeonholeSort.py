def PigeonholeSort(arr):
    n = len(arr)
    min_ = min(arr)
    max_ = max(arr)
    range_ = (max_+1, max_ - min_ + 1)[min_ < 0]
    range_ = max(n,range_)
    p_hole = [0]*range_
    for i in range(n):
        p_hole[arr[i]-min_] += 1

    i = 0
    for count in range(range_):
        while(p_hole[count]>0):
            p_hole[count] -= 1
            arr[i] = count + min_
            i += 1


if __name__ == "__main__":
    arr = [1,5,3,8,2,6,7,33,9,0]
    print(arr)
    PigeonholeSort(arr)
    print("Sorted Array is {}".format(arr))