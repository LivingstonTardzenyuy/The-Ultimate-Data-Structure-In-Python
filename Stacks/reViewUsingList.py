
#creating node class
class Stack:
    def __init__(self):
        self.list=[]
    
    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return "\n".join(values)
    
    #isEmpty, #isFull #push #pop #peek
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False
        
    #push
    def push(self,value):
        # if (isEmpty):
        self.list.append(value)
    
    #pop
    def pop(self):
        if self.isEmpty():
            return "can't pop from empty list"
        else:
            # return self.list.reverse()
            return self.list.pop()
    
    #peek
    def peek(self):
        return self.list(len(list)-1)

stack=Stack()
# print(stack.isEmpty())

# stack.push(3)
stack.push(6)
stack.push(9)
stack.push(3)
stack.push(5)
stack.push(10)

print(stack)

print("pop elements")
# stack.pop()
print(stack.pop())
# print(stack)
# print(stack)