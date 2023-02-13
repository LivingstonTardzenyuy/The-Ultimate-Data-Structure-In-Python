
class Stack:
    def __init__(self):
        self.list=[]
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)

    #operations in stacks
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    def push(self, value):
        return self.list.append(value)

    def pop(self):
        if self.isEmpty():
            return "no element found"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "no element found"
        else:

            return self.list[len(self.list)-1]
stack=Stack()
print(stack.isEmpty())

stack.push(10)
stack.push(20)
stack.push(30)
print(stack)
print("pop")
print(stack.pop())
print("present elements")
print(stack)
print("peek")
print(stack.peek())