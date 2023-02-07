 #created by kongnyuy livingston on 6/02/2023

 #stack creation
class Stack:
    def __init__(self):
        self.list=[]
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)

    #operations on stack
    #IsEmpty
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
    
    #push
    def push(self,value):
        self.list.append(value)
        return "Successfully inserted"

    #pop
    def popItems(self):
        if self.isEmpty():
            return "can't delete from empty stack"
        else:
            return self.list.pop()
            return self.list.reverse()

    #peek
    def peekElement(self):
        if self.isEmpty():
            return "can't return empty stack"
        else:
            return self.list[len(self.list)-1]
    
    #deleteEntireStack
    def delete(self):
        if self.isEmpty():
            return "can't return empty stack"
        else:
            self.list=None
customStack=Stack()
# print(customStack.isEmpty())
customStack.push(2)
customStack.push(4)
customStack.push(6)
customStack.push(8)
# customStack.push(10)
# customStack.push(12)

print(customStack)
print("remvoing item")
print(customStack.popItems())
print(customStack)

print("printing the peek")
print(customStack.peekElement())
print("the stack")
print(customStack)

print("deleting everyting")
customStack.delete()
print(customStack)