
#we use the pop keyword

myDict={
    'Name':'Kongnyuy',
    'Age':'20',
    'Level':'L400',
    'speciality': 'Machine Learning',
    'company':'works in Google'
}

myDict.pop('Age')
print(myDict)

#we can also use popItem and it return the deleted item

myDict.popitem()
print(myDict)

myDict.clear()
print(myDict)