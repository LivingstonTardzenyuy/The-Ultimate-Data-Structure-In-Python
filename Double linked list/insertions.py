
#creation of constructor class
class Node:
    def __init__(self,value=None):
        self.prev=None
        self.next=None
        self.value=value

#creation of double linked list
class doubleLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
        
    #creation of double linked list
    def creation(self, value):
        nodevalue=Node(value)
        nodevalue.next=None
        nodevalue.prev=None

        self.head=nodevalue
        self.tail=nodevalue
    
    #insertion to double linked list
    def insertion(self,value,location):
        if self.head is None:
            print("no linked list present")
        
        else:
            newNode=Node(value)
            if location==0:
                newNode.prev=None
                newNode.next=self.head
                self.head.prev=newNode
                self.head=newNode

            elif location==1:
                newNode.next=None
                newNode.prev=self.tail
                self.tail.next=newNode
                self.tail=newNode

            else:
                tempNode=self.head
                index=0
                while index<location-1:
                    tempNode=tempNode.next
                    index+=1

                newNode.next=tempNode.next
                newNode.prev=tempNode
                newNode.next.prev=newNode
                tempNode.next=newNode

    #traversing across a linked list
    def travers(self):
        if self.head is None:
            print("no value exist to travers")
        else:
            nodevalue=self.head
            while nodevalue is not None:
                print(nodevalue.value)
            
                nodevalue=nodevalue.next

    #reverse traversal
    def reverseTraverse(self):
        if self.tail is None:
            print("no value exist to travers")
        else:
            nodevalue=self.tail
            while nodevalue is not None:
                print(nodevalue.value)

                nodevalue=nodevalue.prev

    #searching for a node
    def searchNode(self,nodevalue):
        if self.head is None:
            print("no node found to print")
        
        else:
            # node=Node(nodevalue)
            tempNode=self.head

            while tempNode is not None:
                if tempNode.value==nodevalue:
                    print(tempNode.value)

                tempNode=tempNode.next
            print("The node value does not exist")
doubLL=doubleLinkedList()
doubLL.creation(5)
doubLL.insertion(10,0)
doubLL.insertion(15,0)
doubLL.insertion(11,1)
doubLL.insertion(13,1)
doubLL.insertion(15,2)
doubLL.insertion(23,3)
print([node.value for node in doubLL])
doubLL.travers()
print("reverse traversal")
doubLL.reverseTraverse()
print("searching methon")
doubLL.searchNode(10)