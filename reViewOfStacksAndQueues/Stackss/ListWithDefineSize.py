
#stack with limeted size

class Stack:
    def __init__(self,value):
        self.value = value
        self.list=[]


    def __str__(self):
        value=self.list.reverse()
        value=[str(x) for x in self.list]
        return "\n".join(value)

    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def isFull(self):
        if len(self.list)==self.value:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "the stack is already full"
        else:
            return self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "cant't remove from empty list"
        else:
            return self.list.pop()
stack=Stack(10)
# print(stac)
print(stack.isEmpty())
print(stack.isFull())
stack.push(5)
stack.push(10)
stack.push(15)
stack.push(20)
stack.push(25)
stack.push(30)
print(stack)

print("pop element")
print(stack.pop())
print("stack")
print(stack)