

#creating class
class Queue:
    def __init__(self,maxValue):
        self.list=maxValue*[None]
        self.maxValue=maxValue
        self.Top=-1
        self.Start=-1

    def __str__(self):
        value=[str(x) for x in self.list]
        return " ".join(value)

    def isFull(self):
        if self.Start==0 and self.Top+1==self.maxValue:
            return True
        elif self.Top+1 ==self.Start:
            return True
        else:
            return False


    def isEmpty(self):
        if self.Top==-1:
            return True
        else:
            return False

    def Enqueue(self, value):
        if self.isFull():
            return "Can't insert"
        else:
            if self.Top+ 1== self.maxValue:
                self.Top=0
            else:
                self.Top+=1
                if self.Start == -1:            #checking if we have only one element and if the case we must update the Start
                    self.Start = 0
            self.list[self.Top] = value

    def Dequeue(self):
        if self.isEmpty():
            return "No element present"
        else:
            value=self.Start
            firstElement=self.list[self.Start]
            if self.Start+1==self.maxValue:
                self.Start=0
            elif self.Start==self.Top:
                self.Start=-1
                self.Top=-1
            else:
                self.Start+=1
            # return self.Start=value
            self.list[value]=None
            return firstElement
            return self.list

    def peek(self):
        if self.isEmpty():
            return "No element present"
        else:
            return self.list[self.Start]

    def delete(self):
        if self.isEmpty():
            return "No element foun to delete"
        else:
            self.list=None
            return self.list
# maxElement=int(input("enter the max value:"))
queue=Queue(10)
print(queue.isEmpty())
print(queue.isFull())
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
print(queue)
print("Dequeue")
print(queue.Dequeue())
print(queue)
print(queue.peek())
print("deleteted")
print(queue.delete())