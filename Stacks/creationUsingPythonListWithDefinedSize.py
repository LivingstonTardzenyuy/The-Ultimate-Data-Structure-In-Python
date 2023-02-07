 #created by kongnyuy livingston on 6/02/2023

#class
class Stack:
    def __init__(self,maxValue):
        self.maxValue=maxValue
        self.list=[]
    
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)


    #opertions

    #isEmpty
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    #isFull
    def isFull(self):
        if len(self.list)==self.maxValue:
            return True
        else:
            return False
    #push
    def push(self,value):
        if self.isFull():
            return "can't push becuase stack is full"
        else:
            self.list.append(value)
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "can't pop from an empty stack"
        else:
            return self.list.pop()

    #peek
    def peek(self):
        if self.isEmpty():
            return "can't pop from an empty stack"
        else:
            return self.list[len(self.list)-1]

    #delete
    def delete(self):
        self.list=[]

customStack=Stack(10)
# print(customStack.isEmpty())
# print(customStack.isFull())

customStack.push(10)
customStack.push(20)
customStack.push(30)
customStack.push(40)

print(customStack)
print("pop element")
print(customStack.pop())
print("all elements")
print(customStack)
print("peek element")
print(customStack.peek())