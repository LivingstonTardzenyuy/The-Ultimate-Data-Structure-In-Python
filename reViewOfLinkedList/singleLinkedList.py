#created by Kongnyuy Livingston Tardzenyuy on 03/02/2023


#creating a constructor class
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

    
#creation of linked list
class singleLinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    #function to display information on the console
    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next

    #inserting function
    def insertion(self,value,location):
        nodeValue=Node(value)
        if self.head is None:
            self.head=nodeValue
            self.tail=nodeValue

        else:
            if location==0:
                nodeValue.next=self.head
                self.head=nodeValue
                
            elif location==1:
                nodeValue.next=None
                self.tail.next=nodeValue
                self.tail=nodeValue

            else:
                node=self.head
                index=0 
                while index<location-1:
                    node=node.next
                    index+=1
                
                tempNode=node.next

                node.next=nodeValue
                nodeValue.next=tempNode

    #traversing
    def traverse(self):
        if self.head is None:
            print("no linked list found to traverse")
        
        else:
            tempNode=self.head

            while tempNode is not None:
                print(tempNode.value)
                tempNode=tempNode.next
            return "no node found"

    #searching function 
    def search(self,nodeValue):
        if self.head is None:
            print("no value present")

        else:
            tempNode=self.head
            while tempNode is not None:
                if tempNode.value==nodeValue:
                    return tempNode.value
                
                tempNode=tempNode.next
                # print("the value is not found")
            
            return "the linked list does not exist"
        

    #deleting function
    def deleting(self,location):
        if self.head is None:
            print("no head value found")
        
        else:
            if location==0:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None

                else:
                    self.head=self.head.next

            elif location==1:
                if self.head==self.tail:
                    self.head=None
                    self.tail=None

                else:
                    nodevalue=self.head
                    while nodevalue is not None:
                        if nodevalue.next==self.tail:
                            break
                        nodevalue=nodevalue.next
                    nodevalue.next=None
                    self.tail=nodevalue
                    return "node value does not exist"      
                
            else:
                nodevalue=self.head
                index=0
                while index<location-1:
                    nodevalue=nodevalue.next
                    index+=1
                
                temNodevalue=nodevalue.next

                nodevalue.next=temNodevalue.next
    
    #deleting entire linked list
    def deletingAll(self):
        if self.head is None:
            return "no linked list present"
        else:
            self.head=None
            self.tail=None
singleL=singleLinkedlist()
singleL.insertion(9,0)
singleL.insertion(10,0)
singleL.insertion(20,1)
singleL.insertion(50,1)
singleL.insertion(40,3)

print([node.value for node in singleL])
# singleL.search(10)
# print(singleL.search(400))

singleL.deleting(2)
print([node.value for node in singleL])

singleL.deletingAll()
print([node.value for node in singleL])