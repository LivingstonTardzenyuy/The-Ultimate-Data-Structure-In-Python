#created by kongnyuy livingstone tardzenyuy on 05/02/2023


from random import randint
#creation of constructor class
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

    #we create an str function to represent the string representatio of our linked list
    def __str__(self):
        return str(self.value)      #we call the value so the user prints it

    
class linkedList:
    def __init__(self, values =None):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    def __str__(self):
        values=[str(x.value) for x in self]
        return '-> '.join(values)

    def __len__(self):
        result=0
        tempNode=self.head
        while tempNode:
            result+=1
            tempNode=tempNode.next
        return result

    def addition(self,value):
        if self.head is None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
        
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return self.tail
        
    def generateRandom(self,n,min_value,max_value):
        self.head=None
        self.tail=None
        for i in range(n):
            self.addition(randint(min_value,max_value))    
        return self
     
linkL=linkedList()
linkL.generateRandom(10,10,30)
print(linkL) 
print(len(linkL ))