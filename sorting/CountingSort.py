# works for negative number also
def CountingSort(arr):
    n = len(arr)
    min_ = min(arr)
    if(min_>=0):
        min_=0
    max_ = max(arr)
    t = (n,max_-min_+1)[min_<0]
    # count array
    count = [0]*t
    for i in arr:
        count[i-min_] += 1
    # preprocess count array
    for i in range(1,t):
        count[i] = count[i]+count[i-1]
    # create the sort array
    output = [0]*n
    # inplace sorting arr[::-1]
    for i in arr[::-1]:
        count[i-min_] = count[i-min_]-1
        output[count[i-min_]] = i
    return output
        


if __name__ == "__main__":
    # array content is less than the length of array
    arr = [1,4,-5,4,1,2,3] 
    print(arr)
    output = CountingSort(arr)
    print("Sorted array is {}".format(output))