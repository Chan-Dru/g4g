# works for negative number also
def CountingSort(arr):
    n = len(arr)
    min_ = min(arr)
    if(min_>=0):
        min_=0
    max_ = max(arr)
    t = (max_+1,max_-min_+1)[min_<0]
    t = max(t,n)
    # count array
    count = [0]*t
    print(t,count)
    for i in arr:
        count[i-min_] += 1
    print(count)
    # preprocess count array
    for i in range(1,t):
        count[i] = count[i]+count[i-1]
    print(count)
    # create the sort array
    output = [0]*n
    # inplace sorting arr[::-1]
    for i in arr[::-1]:
        print(i,i-min_,count[i-min_])
        count[i-min_] = count[i-min_]-1
        output[count[i-min_]] = i
    return output
        

def countSort(arr):
    t = max(arr)+1
    min_ = (0,min(arr))[min(arr)<0]
    n = len(arr)
    t = max(n,t-min_)
    count = [0]*t

    for i in arr:
        count[i-min_] += 1

    output = [0]*n
    j = 0
    for i in range(t):
        temp = count[i]
        while(temp):
            output[j] = i+min_ 
            temp -= 1
            j = j+1
    return output
        


if __name__ == "__main__":
    # array content is less than the length of array
    arr = [0,2,-2,33,4,4,6] 
    print(arr)
    # output = CountingSort(arr)
    output = countSort(arr)
    print("Sorted array is {}".format(output))