#created by Kongnyuy Livingston Tardzenyuy on 03/02/2023

#constructor
class Node:
    def __init__(self,value=None):
        self.next=None
        self.value=value

#creating our class
class CircularLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

            if node==self.tail.next:
                break
        
    #creation of circular linked list
    def creation(self,nodeValue):
        node=Node(nodeValue)
        node.value=nodeValue
        node.next=node

        self.head=node
        self.tail=node 

    #insertion in circular linked list
    def insertionFunction(self,value,location):
        nodevalue=Node(value)
        if self.head is None:
            # return "no node value found"
            self.head=nodevalue
            self.tail=nodevalue
        else:
            
            if location==0:
                nodevalue.next=self.head
                self.head=nodevalue
                self.tail.next=nodevalue

            elif location==1:
                nodevalue.next=self.tail.next
                self.tail.next=nodevalue
                self.tail=nodevalue

            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1

                temptempNode=tempNode.next
                tempNode.next=nodevalue
                nodevalue.next=temptempNode
                # nodevalue.next=temptempNode

                # tempNode.next=temptempNode.next
    
    #traversing 
    def traverse(self):
        if self.head is None:
            print("no head found")
        else:
            tempNode=self.head
            while tempNode:        
                print(tempNode.value)
                tempNode=tempNode.next
                if tempNode==self.tail.next:
                    break

    
    #searching function
    def searching(self,searchingValue):
        nodevalue=self.head
        while nodevalue is not None:
            if (nodevalue.value==searchingValue):
                print(nodevalue.value)
            nodevalue=nodevalue.next
            
            if nodevalue.next==self.tail.next:
                return "the node value does not exist"
        
        # print("no value found")

    #deleting function
    def deleting(self,location):
        if self.head is None:
            return "no linked list found"
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                
                else:
                    self.head=self.head.next
                    self.tail.next=self.head

            elif location==1:
                if self.tail==self.head:
                    self.tail=None
                    self.head=None
                else:
                    tempNode=self.head
                    while tempNode is not None:
                        if tempNode.next==self.tail:
                            break

                        tempNode=tempNode.next
                    tempNode.next=self.tail.next
                    # self.tail.next=tempNode
                    self.tail=tempNode

            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                
                temptempNode=tempNode.next

                tempNode.next=temptempNode.next

    #deleting entire linked list
    def deleteAll(self):
        if self.head is None:
            print("no elements found to delete")
        
        else:
            self.head=None
            self.tail=None
circularLL=CircularLinkedList()
circularLL.insertionFunction(10,0)
circularLL.insertionFunction(20,0)
circularLL.insertionFunction(60,1)
circularLL.insertionFunction(100,1)
circularLL.insertionFunction(30,2)
print([node.value for node in circularLL])

circularLL.traverse()

circularLL.searching(60)

print("deleting")
circularLL.deleting(1)
circularLL.deleting(3)
print([node.value for node in circularLL])

circularLL.deleteAll()
print([node.value for node in circularLL])