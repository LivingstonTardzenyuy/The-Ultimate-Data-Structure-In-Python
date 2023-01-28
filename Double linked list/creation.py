# constructor class
class Node:
    def __init__(self, value=None):
        self.next = None
        self.prev = None
        self.value = value


# class creation
class doubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # printing double linked list
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    # creation of double linked list
    def creation(self, nodeValue):
        node = Node(nodeValue)
        node.next = None
        node.prev = None

        # creating connecting between head, tail and the nodevalue
        self.head = node
        self.tail = node

    # insertion into double linked list
    def insertion(self, value, location):

        if self.head is None:
            print(" no circular linked list found")
        
        else:
            nodevalue=Node(value)
            if location==0:
                nodevalue.prev=None
                nodevalue.next=self.head
                nodevalue.next.prev=nodevalue
                self.head=nodevalue

            elif location==1:
                nodevalue.next=None
                nodevalue.prev=self.head
                self.tail.next=nodevalue
                self.tail=nodevalue

            else:
                index=0
                tempNode=self.head
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1

                nodevalue.next=tempNode.next
                nodevalue.prev=tempNode
                tempNode.next=nodevalue

    #traversing function from 1 to x
    def traverse(self):
        if self.head is None:
            print("no linked list found to print")
        else:
            tempNode=self.head
            while tempNode is not None:
                print(tempNode.value)
                tempNode=tempNode.next
            # print("no head found")

    #traversing from x to 1
    def reverseTraversal(self):
        if self.tail is None:
            print("no linked list found")
        else:
            tempNode=self.tail
            while tempNode is not None:
                print(tempNode.value)
                tempNode=tempNode.prev
    
    #searching function
    def searching(self,nodeValue):
        if self.head is None:
            print("no node found")
        else:
            tempNode=self.head
            while tempNode is not None:
                if tempNode.value==nodeValue:
                    print(tempNode.value)
                
                tempNode=tempNode.next

            print("no node found") 

    #deletion function
    def deletion(self,location):
        if self.head is None:
            print("no linked list present")
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                
                else:
                    self.head=self.head.next
                    self.head.prev=None
            
            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None
                
                else:
            
                    self.tail=self.tail.prev
                    self.tail.next=None
                    
                    # self.head
            
            else:
                tempNode=self.head
                index=0
                while index<location:
                    tempNode=tempNode.next
                    index+=1
                
                tempNode.next=tempNode.next.next
                tempNode.next.prev=tempNode
    
    #deleting entire linked list
    def deleteAll(self):
        if self.head is None:
            print("no elements found to delelte")
        
        else:
            self.head=None
            self.tail=None
doubleLL = doubleLinkedList()
doubleLL.creation(5)
doubleLL.insertion(10, 0)
doubleLL.insertion(20,0)
doubleLL.insertion(60,2)
doubleLL.insertion(2000,3)
doubleLL.insertion(30, 1)
doubleLL.insertion(100,1)
print([node.value for node in doubleLL])
print("traversing forward")
doubleLL.traverse()
print("traversing backward")
doubleLL.reverseTraversal()

print("searching function")
doubleLL.searching(30)
# searchingValue=int(input("enter the value to search"))
# doubleLL.searching(searchingValue)

print("deletion function")
doubleLL.deletion(0)
print([node.value for node in doubleLL])
doubleLL.deletion(3)
print([node.value for node in doubleLL])

print("all deletion")
doubleLL.deleteAll()