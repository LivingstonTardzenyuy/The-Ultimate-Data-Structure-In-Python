
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)

class linkedList:
    def __init__(self):
        # self.list=[]
        self.head=None
        self.tail=None

    def __iter__(self):
        top=self.head
        while top:
            yield top
            top=top.next

class Queue:
    def __init__(self):
        self.linkedL=linkedList()

    def __str__(self):
        value = [str(x) for x in self.linkedL]
        return " ".join(value)

    def isEmpty(self):
        if self.linkedL.head==None:
            return True
        else:
            return False
    def Enqueue(self,value):
        nodevalue = Node(value)
        if self.linkedL.head==None:
            self.linkedL.head=nodevalue
            self.linkedL.tail=nodevalue

        self.linkedL.tail.next=nodevalue
        self.linkedL.tail=nodevalue

    def Deqeue(self):
        remove=self.linkedL.head
        if self.linkedL.head==None:
            self.linkedL.head=None
            self.linkedL.tail=None
        else:
            self.linkedL.head=self.linkedL.head.next
        return remove

    def peek(self):
        return self.linkedL.head.value
queue=Queue()
queue.Enqueue(10)
queue.Enqueue(20)
queue.Enqueue(30)
queue.Enqueue(40)
# print(queue.isEmpty())
print(queue)
print("remvoe")
print(queue.Deqeue())
print("queue")
print(queue)
print(queue.peek())