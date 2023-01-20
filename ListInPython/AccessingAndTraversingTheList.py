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

    def _iter_(self)
        node = self.head
        while node:
            yield node
            node = node.next

    # insert in linked list


# creating object of the class.
# node1=Node(1)
# node2=Node(2)
# node3=Node(3)
# sslinklist.head=node1
# sslinklist.head.next=node2
# sslinklist.tail=node2


sslinklist = singleLinkedList()
print([node.value for node in sslinklist])