"""
Online Array 
Input: 5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4
Output: 5.0
        10.0
        5.0
        4.0
        3.0
        4.0
        5.0
        6.0
        7.0
        6.5
        7.0
        6.5
"""
class heapq():
    def __init__(self,heap,comparator):
        self.heap = heap
        self.comparator = comparator
    
    def heapify(self,i,n):
        index = i
        l = 2*i
        r = 2*i +1
        if l<n and self.comparator(self.heap[l],self.heap[index]):
            index = l
        if r <n and self.comparator(self.heap[r],self.heap[index]):
            index = r
        if index != i:
            self.heap[i],self.heap[index] = self.heap[index],self.heap[i]
            self.heapify(index,n)

    def heapMe(self):
        n = len(self.heap)
        for i in range(n//2,-1,-1):
            self.heapify(i,n)
    
    def insert(self,key):
        self.heap.append(key)
        self.heapMe()
    
    def extract(self):
        item = self.heap.pop(0)
        self.heapMe()
        return item
    
    def top(self):
        return self.heap[0]

def signum(l,r):
    if l==r:
        return 0
    return (-1,1)[l>r]

def median(i,m):
    case = signum(len(MaxHeap.heap),len(MinHeap.heap))
    if case == 1: # maxHeap greater than minHeap
        if i<m:
            MinHeap.insert(MaxHeap.extract())
            MaxHeap.insert(i)
        else:
            MinHeap.insert(i)
        m = (MinHeap.top() + MaxHeap.top())/2
        yield m 
    elif case  == 0: # maxHeap equal to minHeap
        if i<m:
            MaxHeap.insert(i)
            m = MaxHeap.top()
            yield m
        else:
            MinHeap.insert(i)
            m = MinHeap.top()
            yield m
    else: # maxHeap lesser than minHeap
        if i<m:
            MaxHeap.insert(i)
        else:
            MaxHeap.insert(MinHeap.extract())
            MinHeap.insert(i)
        m = (MinHeap.top() + MaxHeap.top())/2
        yield m


if __name__ == "__main__":
    a = [5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]

    smallest = lambda a,b: a<b
    largest = lambda a,b: a>b
    MaxHeap = heapq([],largest)
    MinHeap = heapq([],smallest)

    m = 0
    stream =[]
    for i in a:
        stream.append(i)
        m = next(median(i,m))
        print("The median of array {} is {}".format(stream,m))
