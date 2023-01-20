
#create a constructor class
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None


#create a single linked list
class ssll:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    #inserting value into ssll
    def insertIntoList(self,value,location):
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
                nodeIncrement=self.head
                index=0
                while index<location-1:
                    nodeIncrement=nodeIncrement.next
                    index+=1

                nodeIncrementnext=nodeIncrement.next

                nodeIncrement.next=nodeValue
                nodeValue.next=nodeIncrementnext

    #traversing through a sslink list and printing all values
    def traverse(self):
        # nodeValue=self.head

        if self.head is None:
            print("enter linked list")
        else:
            while self.head is not None:
                print(self.head.value)
                self.head=self.head.next

    def searchValue(self,nodeValue):
        # searchValue=Node(va lue)?
        if self.head is None:
            return "no elements found in the linked list"
        else:
            node=self.head
            while node is not None:
                if node.value==nodeValue:
                    # nodevalue=nodevalue.next
                    return node.value
                else:
                    node=node.next
            return "the value does not exiist"
ss=ssll()
ss.insertIntoList(8,0)
ss.insertIntoList(9,0)
ss.insertIntoList(1,1)
ss.insertIntoList(1,1)
ss.insertIntoList(7,2)
ss.insertIntoList(3,3)
# ss.traverse()
print([node.value for node in ss])
# ss.traverse()
print(ss.searchValue(0))
# ss.searchValue(9)