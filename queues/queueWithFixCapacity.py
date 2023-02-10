#class
class Queue:
    def __init__(self,maxLength):
        self.list=maxLength*[None]
        self.maxLength=maxLength
        self.Top=-1
        self.Start=-1
    
    def __str__(self):
        values=[str(x) for x in self.list]
        return " ".join(values) 

    
    #operations
    def isFull(self):
        if self.Top+1==self.Start:
            return True
        elif self.Start==0  and self.Top+1 ==self.maxLength:
            return True
        else:
            return False

    def isEmpty(self):
        if self.Top==-1:
            return True
        else:
            return False

    def Enqueue(self,value):
        if self.isFull():
            return "cant't insert because the Queue is Full"
        else:
            if self.Top+1 == self.maxLength:
                self.Top=0
            else:
                self.Top+=1
                if self.Start==-1:      #checking whether an element already exist in the queue
                    self.Start=0
            self.list[self.Top]=value
    def Dequeue(self):
        if self.isEmpty():
            return "can't delete from empty queue"
        else:
            firstValue=self.list[self.Start]
            # self.Start = self.list[0]
            if self.Start == self.Top:
                self.Start = -1
                self.Top = -1
            elif self.Start + 1 == self.maxLength:
                self.Start = 0
            else:
                self.Start += 1
            self.list[self.Start] = None
            return firstValue

queue=Queue(10)
print(queue.isEmpty())
print("enqueue method")

queue.Enqueue(5)
queue.Enqueue(10)
queue.Enqueue(15)
queue.Enqueue(20)
queue.Enqueue(5)
queue.Enqueue(10)
queue.Enqueue(15)
# queue.Enqueue(5)
# queue.Enqueue(10)
# queue.Enqueue(15)
# queue.Enqueue(15)
print(queue)
print("dequee")
print(queue.Dequeue())
print("elements")
print(queue)