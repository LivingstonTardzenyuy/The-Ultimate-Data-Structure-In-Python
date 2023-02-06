#created by kongnyuy livingston tardzenyuy on 6/02/2023 

from create import *

def partioningALinkedList(ll,n):
    currentNode=ll.head
    ll.tail=currentNode
    currentNode.next=None

    while currentNode:
        nextNode=currentNode.next
        currentNode.next=None
        if currentNode.value<n:
            currentNode.next=ll.head
            ll.head=currentNode
        else:
            ll.tail.next=currentNode
            ll.tail=currentNode
        currentNode=nextNode
    
    if ll.tail.next is not None:
        ll.tail.next=None

customLL=linkedList()
customLL.generateRandom(10,0,30)
print(customLL)

partioningALinkedList(customLL,12 )
print(customLL)
    