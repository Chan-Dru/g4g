class Queue:
    def __init__(self,capacity):
        self.queue = [None]*capacity
        self.capacity = capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0

    def isFull(self):
        return self.size == self.capacity
    
    # add item to the rear of queue
    def enqueue(self,key):
        if not self.isFull():
            self.rear = (self.rear+1)%self.capacity
            self.queue[self.rear] = key
            self.size +=1
        else:
            print("Queue is Full, keep waiting !!!")
    
    # remove item from the front of queue
    def dequeue(self):
        item = None
        if not self.isEmpty():
            item, self.queue[self.front] = self.queue[self.front], item
            self.front = (self.front+1)%self.capacity
            self.size -= 1
        return item
    
    # return item in front of queue
    def QFront(self):
        if not self.isEmpty():
            return self.queue[self.front]
        return None

    # return item in rear of queue
    def QRear(self):
        if not self.isEmpty():
            return self.queue[self.rear]
        return None

if __name__ == "__main__":
    arr = [4,7,2,1,5,6,3,8,0,9]
    capacity = 5
    q = Queue(capacity)
    for i in arr[:6]:
        print(i)
        q.enqueue(i)
    print(q.QFront())
    print(q.QRear())
    print(q.dequeue(),end = " ")
    print(q.dequeue(),end = " ")
    print(q.QFront())
    print(q.QRear())
    for i in arr[7:]:
        print(i)
        q.enqueue(i)
    print(q.QFront())
    print(q.QRear())
    for i in range(q.size):
        print(q.dequeue())

    
