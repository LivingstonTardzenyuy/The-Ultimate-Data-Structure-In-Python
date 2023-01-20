#a string is a sequence  characters while a list is compose of letters

#converting a string to a list
a="kongnyuy livingston tardzenyuy"
letters=list(a)
print(letters)

#we can also convert a sentece to individual words
b="Kongnyuy Livingston tardzenyuy is a machine learning engineer in Cyber Security"
print(b.split())


#we cant also convert a list to a string using join() keyword
letter=['a','b','c','d','e']
lis=[""]
# print(letter.count()
print(lis.join(letter))
