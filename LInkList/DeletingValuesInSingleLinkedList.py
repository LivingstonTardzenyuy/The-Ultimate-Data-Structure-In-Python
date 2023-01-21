
#constructor
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

#class
class singleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    #inserting method
    def insert(self,value,location):
        nodeValue=Node(value)
        if self.head is None:
            self.head=nodeValue
            self.tail=nodeValue

        else:
            if location==0:
                self.head=nodeValue
                nodeValue=self.head

            elif location==1:
                nodeValue.next=None
                self.tail.next=nodeValue
                self.tail=nodeValue

            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1

                tempNodeNode=tempNode.next

                tempNode.next=nodeValue
                nodeValue.next=tempNodeNode


    #deleting method
    def deletingmethod(self,location):
        if self.head is None:
            return "no elements found to delete"
        else:
            if location==0:
                if self.head==self.tail:        #only one elements exist
                    self.head=None
                    self.tail=None

                else:                           #multiple elements exist
                    self.head=self.head.next        #connecting the head to our 2nd element thereby removing the first node

            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None

                else:
                    node=self.head
                    while node is not None:
                        if node.next==self.tail:            #we are trying to not the element before the last node
                            # node.next = node
                            break
                        node=node.next

                    node.next=None
                    self.tail=node
            else:
                nodeValue=self.head
                index=0
                while index<location-1:
                    nodeValue=nodeValue.next
                    index+=1

                nodeValueValue=nodeValue.next

                nodeValue.next=nodeValueValue.next

ssl=singleLinkedList()
ssl.insert(3,0)
ssl.insert(4,1)
ssl.insert(9,1)
ssl.insert(2,2)
ssl.insert(12,1)

# deletingMethod(5)
# print(delete)
print([node.value for node in ssl])

ssl.deletingmethod(3)
print([node.value for node in ssl])