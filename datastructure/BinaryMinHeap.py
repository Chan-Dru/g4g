import sys
# import heapq

# implementation of heapq
class heapq():
    def __init__(self):
        self.heap = []
    
    def minHeapify(self,heap,i,n):
        smallest = i
        l = i*2 + 1
        r = i*2 + 2
        if l<n and heap[smallest] > heap[l]:
            smallest = l
        if r<n and heap[smallest] > heap[r]:
            smallest = r
        if i != smallest:
            # print(heap[i], heap[smallest])
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.minHeapify(heap,smallest,n)

    def heapify(self, heap):
        n = len(heap)
        for i in range(n//2+1,-1,-1):
            self.minHeapify(heap,i,n)
        # print(heap)
    
    def heappush(self, heap, e):
        heap.append(e)
        self.heapify(heap)
    
    def heappop(self, heap, i=0):
        e = heap.pop(i)
        self.heapify(heap)
        return e

class MinHeap(heapq):
    def __init__(self):
        super().__init__()
        self.heap = []

    def deleteKey(self, e):
        self.decreaseKey(e,-sys.maxsize)
        self.extractMin()

    def extractMin(self):
        if len(self.heap) == 0:
            return
        return self.heappop(self.heap)

    def decreaseKey(self, e, val):
        self.heap[e] = val
        i = (e-1)//2
        while(i>=0 and self.heap[e] < self.heap[i]):
            self.heap[e] , self.heap[i] = self.heap[i], self.heap[e]
            e = i
            i = (e-1)//2

    def insertKey(self, val):
        self.heappush(self.heap, val)
    
    def getMin(self):
        return self.heap[0]



if __name__ == "__main__":
    # heapObj = heapq()
    # heap = []
    # heapObj.heappush(heap, 3) 
    # heapObj.heappush(heap, 2) 
    # # heapObj.heappop(heap,1) 
    # heapObj.heappush(heap, 15) 
    # heapObj.heappush(heap, 5) 
    # heapObj.heappush(heap, 4) 
    # heapObj.heappush(heap, 45) 
    # print(heap)

    heapObj = MinHeap() 
    heapObj.insertKey(3) 
    heapObj.insertKey(2) 
    heapObj.deleteKey(1)
    heapObj.insertKey(15) 
    heapObj.insertKey(5) 
    heapObj.insertKey(4) 
    heapObj.insertKey(45) 
    print(heapObj.heap)
    heapObj.decreaseKey(4, 1) 
    print(heapObj.heap)
    print(heapObj.extractMin()) 
    print(heapObj.getMin()) 
    
    # heap = []
    # heapq.heappush(heap,3)
    # heapq.heappush(heap,2)
    # heapq.heappop(heap)
    # heapq.heappush(heap,15)
    # heapq.heappush(heap,5)
    # heapq.heappush(heap,4)
    # heapq.heappush(heap,45)
    # print(heap) #[2, 3, 15, 5, 4, 45] [3, 4, 5, 15, 45]