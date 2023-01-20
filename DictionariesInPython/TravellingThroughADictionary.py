#travelling through a dic
#visiting all keys

myDict={
    'Name':'Kongnyuy',
    'Age':'20',
    'Level':'L400',
    'speciality': 'Machine Learning',
    'company':'works in Google'
}

def traverse(Dict):
    for key in myDict:
        print(key,Dict[key])

traverse(myDict)


def searchElement(Dict2,n):
    for search in Dict2:
        if Dict2[search]==n:
           return search,n
        else:
            return 'not found'
element='L400'
print(searchElement(myDict,element))