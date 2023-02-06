#created by kongnyuy livingstone tardzenyuy on 05/02/2023

# Q1. Remove duplicates: write codes to remove duplicates from an unsorted linked list.

from create import *

def removeduplicate(ll):
    currentNode=ll.head
    if currentNode is None:
        return "no linked list present"
    else:
        tempSet=set([currentNode.next.value])
        while currentNode.next is not None:
            if currentNode.next.value in tempSet:
                currentNode.next=currentNode.next.next
            else:
                tempSet.add(currentNode.next.value)
                currentNode=currentNode.next
        print("no linked list present")

customLL=linkedList()
customLL.generateRandom(10,10,30)
print(customLL)

removeduplicate(customLL)
print(customLL)

