# target is 9

# def findSums(arrayNumbers,target,sizeOfList):
arrayNumber=[]
sizeOfLists=int(input("enter the size of the list:"))
for iterator in range(0,sizeOfLists):
    data=int(input("enter an element:"))
    arrayNumber.append(data)

finalAray=arrayNumber
print("the array the user inputted is")
print(finalAray)

targetValue=int(input("enter the targer value:"))
def findPairs(Aray,target):
    for i in range(0,len(Aray)):
        for j in range(i+1,len(Aray)):
            if Aray[i]+Aray[j]==target:
                print(i,j)
            else:
                # print("no occurances")
                break

findPairs(finalAray,targetValue)
