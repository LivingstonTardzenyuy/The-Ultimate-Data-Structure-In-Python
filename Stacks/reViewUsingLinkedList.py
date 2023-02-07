
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None

#class
class LinkedList:
    def __init__(self):
        # self.list=[]
        self.head=None

    # def __str__(self):
    #     values=self.head.reverse()
    #     values=[str(x) for x in values]
    #     return "\n".join(values)
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next


class Stack:
    def __init__(self):
        self.LinkedList=LinkedList()
    
    def __str__(self):
        values=[str(x.value) for x in self.LinkedList]
        return "\n".join(values)
    #operations
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    def push(self,value):
        tempNode=Node(value)        
        tempNode.next=self.LinkedList.head
        self.LinkedList.head=tempNode
    
    def pop(self):
        if self.LinkedList.head.next is None:
            self.LinkedList.head=None
        else:
            self.LinkedList.head=self.LinkedList.head.next

    def peek(self):
        if self.isEmpty():
            return "no elements present to remove"
        else:
            return self.LinkedList.head.value

stack=Stack()
# print(stack.isEmpty())
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
print(stack)

# print("pop element")
# stack.pop()
# print(stack)

print("pop elements")
print(stack.peek())