def FibonacciGenerator(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return FibonacciGenerator(n-1)+FibonacciGenerator(n-2)


def FibonacciSearch_usingGenerator(arr,key):
    m=0
    while(FibonacciGenerator(m)<=len(arr)):
        m=m+1
    offset = -1
    while(FibonacciGenerator(m)>1):
        i = min(offset+FibonacciGenerator(m-2),len(arr)-1)
        if(arr[i]<key):
            m = m-1
            offset = i
        elif(arr[i]>key):
            m = m-2
        if(arr[i]==key):
            return i
    if(FibonacciGenerator(m-1) and arr[offset+1]==key):
        return offset+1
    return -1

def FibonacciSearch(arr,key):
    m=0
    n=len(arr)
    Fib2=0
    Fib1=1
    Fib = Fib1 + Fib2
    while(Fib<=n):
        Fib2=Fib1
        Fib1=Fib
        Fib = Fib1 + Fib2

    offset = -1
    while(Fib>1):
        i = min(offset+Fib2,n-1)
        if(arr[i]<key):
            Fib = Fib1
            Fib1 = Fib2
            Fib2 = Fib-Fib1
            offset = i
        elif(arr[i]>key):
            Fib=Fib2
            Fib1= Fib1-Fib2
            Fib2= Fib - Fib1
        else:
            return i
    if(Fib1 and arr[offset+1]==key):
        return offset+1
    return -1

if __name__ == "__main__":
    arr = [0]
    key = 0
    index = FibonacciSearch_usingGenerator(arr,key)
    if index >= 0 :
        print("key {} is found at index {}".format(key,index))
    else:
        print("key {} is not found in the array".format(key))