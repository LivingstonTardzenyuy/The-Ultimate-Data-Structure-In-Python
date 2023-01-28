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
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                self.head = newNode
                newNode.next = self.head
                self.head.prev = newNode


doubleLL = doubleLinkedList()
doubleLL.creation(5)
doubleLL.insertion(10, 0)
# doubleLL.insertion(20,0)
print([node.value for node in doubleLL])