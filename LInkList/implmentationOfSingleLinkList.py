#created by livingston 09/01/2023

#steps
#1. create the head, tail and initialize the values to null
#2. create a new node and assign a value to it and reference it to null
#3. Link head and tail to the nodes



#created class which contain the value and null references which is a constructor
class Nodevalue:
    def __init__(self, value=None):
        self.value=value
        self.next=None
        

#creating a class and initializing head and tail to null
class SingleLinkList:
    def __init__(self):
        self.head=None
        self.tail=None

    #method to help print the list
    def _iter_(self):
        node=self.head
        while node:
            yield node
            node=node.next
            node+=1


    #insert to linked list
    def insert(self,value,location):
        newNode=Nodevalue(value)

        if self.head is None:
            self.head=newNode
            self.tail=newNode
        
        else:

            #inserting at the begining of the link list
            if location==0:
                newNode.next=self.head
                self.head=newNode

            #addint at the end of a link list
            elif location==1:
                newNode.next=Nodevalue
                self.tail=newNode
                self.tail=newNode   

            #addng at the middle of the link list
            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1

                nextNode=tempNode.next
                tempNode=newNode
                newNode.next=nextNode  
            
SingleLL=SingleLinkList()
SingleLL.insert(1,1)
print([Nodevalue.value for Nodevalue in SingleLL])
