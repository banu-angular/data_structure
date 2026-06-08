class Queue():
    def __init__(self,k):
        self.head = -1
        self.tail= -1
        self.queue = [None]*k
        self.k=k
    def enqueue(self, item):
        if(self.tail==self.k - 1):
            print("Queue is full")        
        elif(self.head==-1):
            self.head=0
            self.tail=0
            self.queue[self.tail]=item
        else:
            self.tail=self.tail+1
            self.queue[self.tail]=item
    def dequeue(self):
        if(self.head==-1):
            print("Queue is empty")
            return
        elif(self.head==self.tail):
            self.head=-1
            self.tail=-1
            return self.queue[self.head]
        else:
            self.head=self.head+1
            return self.queue[self.head-1]
    def peek(self):
        if(self.head==-1):
            print("Queue is empty")
            return
        else:
            return self.queue[self.head]
    def printQueue(self):
        if(self.head==-1):
            print("Queue is empty")
            return
        else:
            for i in range(self.head,self.tail+1):
                print(self.queue[i],end=" ")
            print()

if __name__ == "__main__":
    queue1 = Queue(5)
    queue1.enqueue(23)
    queue1.enqueue(24)
    queue1.enqueue(25)
    print(queue1.dequeue())
    queue1.printQueue()
    queue1.enqueue(26)
    queue1.enqueue(27)
    queue1.enqueue(28)
    queue1.printQueue()
    print(queue1.peek())
    queue1.printQueue()
