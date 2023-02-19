#creating a binary tree using linked list

class BinaryTreeUsingLinkedList:
    def __init__(self, value):
        self.value=value
        self.leftChild=None
        self.rightChild=None

binarytreeusinglikedlist=BinaryTreeUsingLinkedList("Drinks")

cold=BinaryTreeUsingLinkedList("Cold")
hot=BinaryTreeUsingLinkedList("Hot")

fanta=BinaryTreeUsingLinkedList("Fanta")



leftChild=cold
rightChild=hot


binarytreeusinglikedlist.leftChild=leftChild
binarytreeusinglikedlist.rightChild=rightChild

print("preOder traversing")
def preOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        print(rootNode.value)

        #recursive calling
        preOrderTraversal(rootNode.leftChild)
        preOrderTraversal(rootNode.rightChild)
preOrderTraversal(binarytreeusinglikedlist)


print("")
print("inoder traversing")
def inorderTraversal(rootNode):
    if not rootNode:
        return
    preOrderTraversal(rootNode.leftChild)
    print(rootNode.value)
    preOrderTraversal(rootNode.rightChild)

inorderTraversal(binarytreeusinglikedlist)

print("")
print("post order traversing")

def postOderTraversing(rootNode):
    if not rootNode:
        return

    postOderTraversing(rootNode.leftChild)
    postOderTraversing(rootNode.rightChild)
    print(rootNode.value)
postOderTraversing(binarytreeusinglikedlist)