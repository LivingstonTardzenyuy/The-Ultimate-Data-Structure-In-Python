# constructor of the class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# creating a single linked list
class singleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #inserting into single linked list
    def insertIntoSingleLinkedList(self, value, location):
        newNode=Node(value)         #we create a new node base on our class contructor

        #chech if head value is null
        if self.head is None:       #no node found in the linked list
            self.head=newNode
            self.tail=newNode

        else:
            if location==0:             #inserting at begining of linked list
                newNode.next=self.head
                self.head=newNode

            elif location == 1:              #inserting at end of linked list
                newNode.next=None
                self.tail.next=newNode
                self.tail=newNode

            else:                       #at the middle
                tempNode=self.head
                index=0
                while index<location-1:         #looping to look for the current place
                    tempNode=tempNode.next
                    index+=1

                nextNode=tempNode.next          #to know the node before we wnat to insert

                tempNode.next=newNode
                newNode.next=nextNode

    #traversing through a linked list
    def traverseThroughLinkedList(self):
        firstNode=self.head
        index=0
        if self.head is None:
            print("no element exist in our linkedlist")
        else:
            while firstNode is not None:
                print(firstNode.value)
                firstNode=firstNode.next


    #deleting an element from the linked list
    def deleteElement(self, location):
        if self.head is None:
            print("single linked list does not exist")
        
        else:
            if location==0:             #inserting at the begining
                if self.head==self.tail:        #when only one element exist
                    self.head=None
                    self.tail=None
                else:                       #more than one element exist
                    self.head=self.head.next

            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None

                else:
                    nodeLooping=self.head
                    index=0

                    while index<location-1:
                        

                    





sslinklist = singleLinkedList()
#putting elements in our linked list
sslinklist.insertIntoSingleLinkedList(1,1)
sslinklist.insertIntoSingleLinkedList(2,1)
sslinklist.insertIntoSingleLinkedList(3,1)
sslinklist.insertIntoSingleLinkedList(4,1)

#inserting at begineing
sslinklist.insertIntoSingleLinkedList(0,0)

#inserting at middle
sslinklist.insertIntoSingleLinkedList(5,3)
print([node.value for node in sslinklist])


#calling the traverse function
sslinklist.traverseThroughLinkedList()