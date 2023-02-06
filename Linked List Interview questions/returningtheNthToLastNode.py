#created by kongnyuy livingston on 05/02/2023

from create import *

def returningNth(ll,n):
    if ll.head is None:
        return "empty linked list"
    else:
        first=ll.head
        pointer1=first
        pointer2=first

        for i in range(n):
            if pointer2 is None:
                return None
            else:
                pointer2=pointer2.next
            
        while pointer2:
            pointer1=pointer1.next
            pointer2=pointer2.next
        return pointer1

customLL=linkedList()
customLL.generateRandom(10,10,30)
print(customLL)

print(returningNth(customLL,8))
# print(customLL)
