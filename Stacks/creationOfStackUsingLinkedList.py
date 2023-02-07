   #created by kongnyuy livingston on 6/02/2023

#constructor
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
    #     values=self.list.reverse()
    #     values=[str(x) for x in self.list]
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

    #isEmpty
    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False
    
    #push
    def push(self,value):
        nodeValue=Node(value)
        nodeValue.next=self.LinkedList.head
        self.LinkedList.head=nodeValue

    #pop
    def pop(self):
        if self.isEmpty():
            return "There is no element"
        else:
            self.LinkedList.head=self.LinkedList.head.next
    
    #peek
    def peek(self):
        if self.isEmpty():
            return "There is no element"
        else:
            nodevalue=self.LinkedList.head.value
            return nodevalue    
customStack=Stack()
print(customStack.isEmpty())

customStack.push(10)
customStack.push(20)
customStack.push(30)
customStack.push(40)
print(customStack)

print("pop function")
print(customStack.pop())
print("my stack")
print(customStack)

print("peek")
print(customStack.peek())
# print(customStack)