#missing number

myList=[]
for i in range(1,101):
    myList.append(i)

print(myList)

def findMisingNumber(list,num):
    # num=len(myList)
    sum1=100*101/2
    sum2=sum(myList)
    print(sum1-sum2)

findMisingNumber(myList,len(list))