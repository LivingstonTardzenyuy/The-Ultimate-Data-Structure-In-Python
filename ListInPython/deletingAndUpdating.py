characters=['a','b','c','d','e','f','g','i','j']

#updating elements of a list using slice
characters[:3]=['x','y','z']
print(characters)

#we can delete element from alist using pop,delete
print(characters.pop(1))
#using delet
del characters[:2]
print(characters)