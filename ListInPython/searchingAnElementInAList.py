characters=['a','b','c','d','e','f','g','i','j']

#we can search by using the In operator or searching algortithms

#if 'a' in characters:
   # print (characters.index('a'))       #searches for an element and returns the index of the element

#else:
   # print("not found")


#using linear search
def searchElement(characterss, element):
    for i in characterss:
        if i==element:
            return (characterss.index(element))
        
        else:
            return ("not found! sorry")

element=input("enter a letter:")
print(searchElement(['a','b','c','d','e','f','g','i','j'],element))
# print(result)