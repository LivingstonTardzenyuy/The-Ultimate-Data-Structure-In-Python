

class Queues:
    def __init__(self):
        self.tempQueues=[]

    def __str__(self):
        # values=self.tempQueues()
        values=[str(x) for x in self.tempQueues]
        return " ".join(values)



    #operations
    def isEmpty(self):
        if self.tempQueues=="":
            return True
        else:
            return False

    def Enqueue(self,value):
        self.tempQueues.append(value)

    def Dequeue(self):
        if self.isEmpty():
            return "Can't delete from empty queue"
        else:
            return self.tempQueues.pop(0)           #to remove first element

    def peek(self):
        if self.isEmpty():
            return "Can't delete from empty queue"
        else:
            return self.tempQueues[0]
    
    def delete(self):
        self.tempQueues=None
queues=Queues()
# print(queues.isEmpty())

queues.Enqueue(10)
queues.Enqueue(20)
queues.Enqueue(30)
queues.Enqueue(40)
queues.Enqueue(50)
print(queues)
print("Deleted elements")
print(queues.Dequeue())
print("the Queue")
print(queues)

print("peek element")
print(queues.peek())

print(queues.delete())