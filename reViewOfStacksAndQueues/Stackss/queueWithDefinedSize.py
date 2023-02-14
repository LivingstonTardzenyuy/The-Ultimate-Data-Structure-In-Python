
class Queue:
    def __init__(self, maxvalue):
        self.list=maxvalue* [None]
        self.maxvalue=maxvalue
        self.start=-1
        self.top=-1

    def __str__(self):
        value=[str(x) for x in self.list]
        return " ".join(value)

    def isEmpty(self):
        if self.top==-1:
            return True
        else:
            return False

    def isFull(self):
        if self.start==0 and self.top+1==self.maxvalue:
            return True
        elif self.top+1 == self.start:
            return True
        else:
            return False

    def Enqueue(self,value):
        if self.isFull():
            return "No space found"
        else:
            if self.top+1==self.maxvalue:
                self.top=0
            else:
                self.top+=1
                if self.start==-1:
                    self.start=0
            self.list[self.top]=value

    def Dequeue(self):
        if self.isEmpty():
            return "No element present"
        else:
            begin=self.start
            if self.start+1==self.maxvalue:
                self.start=0
            elif self.start==self.top:
                self.start=-1
                self.top=-1
            else:
                self.start +=1
            self.list[begin]=None

    def peek(self):
        return self.list[self.start]
queue=Queue(10)
# print(queue.isFull())
# print(queue.isEmpty())

queue.Enqueue(5)
queue.Enqueue(10)
queue.Enqueue(15)
queue.Enqueue(20)

print(queue)

# print(queue.Dequeue())
print(queue.Dequeue())

print("quue")
print(queue)
print(queue.peek())