#created by kongnyuy livingston on 10/02/2023

#constructor
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

    def __str__(self):
        return str(self.value)

#linked lisst class
class likedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

class Queue:
    def __init__(self):
        self.linkedlist=likedList()

    def __str__(self):
        values=[str(x) for x in self.linkedlist]
        return  " ".join(values)

    def isEmpty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False
    def Enqueue(self,value):
        node = Node(value)
        if self.isEmpty():
            self.linkedlist.head=node
            self.linkedlist.tail=node
        else:
            self.linkedlist.tail.next=node
            self.linkedlist.tail=node

    def Dequeue(self):
        if self.isEmpty():
            return "No element found to remove"
        else:
            tempNode=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next
            return tempNode

    def peek(self):
        return self.linkedlist.head.value
queue=Queue()
print(queue.isEmpty())
queue.Enqueue(5)
queue.Enqueue(10)
queue.Enqueue(15)
queue.Enqueue(20)
queue.Enqueue(25)
queue.Enqueue(30)
print(queue)
print("Dequeue elements")
print(queue.Dequeue())
print(queue)
print("the peek value is ")
print(queue.peek())