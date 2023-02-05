#designed by kongnyuy livingston Tardzenyuy 03/02/2023

#constructor class
class Node:
    def __init__(self,value=None):
        self.next=None
        self.prev=None
        self.value=value
#class
class doubleCircularLinkedList:
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
    
    #creation
    def creation(self,nodevalue):
        newNode=Node(nodevalue)
        # node.value=nodevalue
        self.head=newNode
        self.tail=newNode

        newNode.next=newNode
        newNode.prev=newNode

    #insertion
    def insertion(self,value,location):
        nodeValue=Node(value)
        if self.head is None:
            print("no node found to print")
        
        else:
            if location==0:
                nodeValue.next=self.head
                nodeValue.prev=self.tail
                self.head=nodeValue
                self.head.next.prev=nodeValue
            
            elif location==1:
                nodeValue.next=self.head
                nodeValue.prev=self.tail
                self.head.prev=nodeValue
                self.tail.next=nodeValue
                self.tail=nodeValue

            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                
                temptempNode=tempNode.next

                nodeValue.next=tempNode.next
                nodeValue.prev=tempNode
                tempNode.next=nodeValue
                nodeValue.next.prev=nodeValue

    #traversing
    def traverse(self):
        if self.head is None:
            print("no node found to traverse")
        else:
            tempNode=self.head
            while tempNode is not None:

                print(tempNode.value)
                tempNode=tempNode.next

                if tempNode==self.tail.next:
                    break
    
    #searching 
    def searchingFunction(self,value):
        if self.head is None:
            print("no node found to delete")
        else:
            # nodevalue=Node(value)
            tempNode=self.head
            while tempNode is not None:
                if tempNode.value==value:
                    print(tempNode.value)
                      
                # to prevent infinite loop
                if tempNode==self.tail:      
                    print("value not found")
                tempNode=tempNode.next 

    #deleting function
    def deletion(self,location):
        if self.head is None:
            return "no value present to delelete"
        else:
            if location==0:
                # nodeValue=Node()
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                    self.head.prev=None
                    self.head.next=None
                else:
                    self.head=self.head.next
                    self.head.prev=self.tail
            
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                    self.head.prev=None
                    self.head.next=None
                else:
                    self.tail=self.tail.prev
                    self.tail.next=self.head

            else:
                index=0
                tempNode=self.head
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1
                
                temptempNode=tempNode.next

                tempNode.next=temptempNode.next
                temptempNode.prev=tempNode

doubleCLL=doubleCircularLinkedList()
doubleCLL.creation(9)

doubleCLL.insertion(10,0)
doubleCLL.insertion(20,0)
doubleCLL.insertion(30,0)
doubleCLL.insertion(50,1)
doubleCLL.insertion(60,1)
doubleCLL.insertion(70,2)
print([node.value for node in doubleCLL])

# doubleCLL.traverse()
# doubleCLL.searchingFunction(50)

doubleCLL.deletion(0)
doubleCLL.deletion(1)
doubleCLL.deletion(2)
print([node.value for node in doubleCLL])