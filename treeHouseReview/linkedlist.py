
#node value constructor
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __inter__(self):
        value=self.head
        while value:
            yield value
            value=value.next

    def insertion(self,value):
        if self.head==self.tail:
            self.head=value
            self.tail=value

linkedIn=LinkedList()
linkedIn.insertion(10)
print(linkedIn)