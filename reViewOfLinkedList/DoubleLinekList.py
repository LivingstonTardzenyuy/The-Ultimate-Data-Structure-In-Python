
#created by Kongnyuy Livingston Tardzenyuy on 03/02/2023
class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
        self.prev=None

#class
class doubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    #creation
    def creation(self,value):
        nodeValue=Node(value)
        # nodeValue.value=nodeValue
        nodeValue.next=None
        nodeValue.prev=None

        self.head=nodeValue
        self.tail=nodeValue

    #insertion
    def insertion(self,value,location):
        if self.head is None:
            return "no linked list present"
        else:
            nodeValue=Node(value)
            if location==0:
                
                nodeValue.prev=None
                nodeValue.next=self.head
                self.head.prev=nodeValue
                self.head=nodeValue
            
            elif location==1:
                nodeValue.next=None
                nodeValue.prev=self.tail
                self.tail.next=nodeValue
                self.tail=nodeValue
                
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                
                temptemptNode=tempNode.next

                nodeValue.next=tempNode.next
                nodeValue.prev=tempNode
                tempNode.next=nodeValue
                temptemptNode.prev=nodeValue


    #Traversing farword
    def traverseFarword(self):
        if self.head is None:
            return "no linked list present"
        
        else:
            tempNode=self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode=tempNode.next

    #traversing backward
    def traversebackword(self):
        if self.head is None:
           return "no linked list present"
        
        else:
            tempNode=self.tail
            while tempNode is not None:
                print(tempNode.value)
                tempNode=tempNode.prev

    #deleting node
    def deleting(self,location):
        if self.head is None:
            return "no node found to delete"
        
        else:
            if location==0:
                self.head=self.head.next
                self.head.prev=None

            elif location==1:
                tempNode=self.head
               
                while tempNode is not None:
                    if tempNode.next==self.tail:
                        break
                    tempNode=tempNode.next
                self.tail=tempNode.prev
                tempNode.next=None
                    
            else:
                index=0
                tempNode=self.head
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                
                temptemptNode=tempNode.next

                tempNode.next=temptemptNode.next
                temptemptNode.prev=tempNode
doubelLL=doubleLinkedList()
doubelLL.creation(9)
doubelLL.insertion(10,0)
doubelLL.insertion(20,0)
doubelLL.insertion(50,1)
doubelLL.insertion(60,1)
doubelLL.insertion(4,2)
doubelLL.insertion(80,3)

print([node.value for node in doubelLL])

print("farward traversing")
# doubelLL.traverseFarword()

print("backward traversing")
# doubelLL.traversebackword()

doubelLL.deleting(0)
doubelLL.deleting(1)
doubelLL.deleting(2)
print([node.value for node in doubelLL])