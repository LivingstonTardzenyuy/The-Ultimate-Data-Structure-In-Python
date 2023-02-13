#constructor
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=next

#class
class linkedlist:
    def __init__(self):
        self.head=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
#class Stack
class Stack:
    def __init__(self):
        self.linkedL=linkedlist()

    def __str__(self):
        values=[str(x.value) for x in self.linkedL]
        return "\n".join(values)
    def isEmpty(self):
        if self.linkedL.head==None:
            return True
        else:
            return False

    def push(self, value):
        node=Node(value)
        node.next=self.linkedL.head
        self.linkedL.head=node
        # return self.linkedL

    def pop(self):
        if self.isEmpty():
            return "Can't delete from empty stack"
        else:
            firstValue=self.linkedL.head.value
            self.linkedL.head=self.linkedL.head.next
            return firstValue

    def peek(self):
        if self.linkedL.head==None:
            return "No element found"
        else:
            return self.linkedL.head.value

    def delete(self):
        self.linkedL.head=None
stack=Stack()
print(stack.isEmpty())

stack.push(10)
stack.push(20)
stack.push(30)
print(stack)

print("remove element")
print(stack.pop())
print("Stack")
print(stack)
print("peek element")
print(stack.peek())
print(stack.delete())