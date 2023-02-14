#class
class Queue:
    def __init__(self):
        self.list= []

    def __str__(self):
        value=[str(x) for x in self.list]
        return " ".join(value)
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def Enqueue(self, value):
        return self.list.append(value)

    def Dequeue(self):
        if self.isEmpty():

            return "NO element found to delete"
        else:
            return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            return "NO element found to delete"
        else:
            return self.list[0]

    def delete(self):
        self.list=None
queue=Queue()
print(queue.isEmpty())
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
print(queue)
print("remove element")
print(queue.Dequeue())
print("queue")
print(queue)
print(queue.peek())
print(queue.delete())