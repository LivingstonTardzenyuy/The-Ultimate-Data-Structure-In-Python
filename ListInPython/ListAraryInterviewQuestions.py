#find the average temperature from the user input

num1=int(input("how many day's temperature ?"))

count=0
sum=0

tempList=[]
while count<num1:
    nextday=int(input("Day" + str(count+1) + "'s high temp:"))
    # if(num1>nextday):
    #     pr5int ("the value bigger than the user input is" + str(num1))
    # else:
    #     print("the value bigger than the user input is" +str(nextday))

    tempList.append(nextday)        #adding data to our list
    
    sum+=tempList[count]
    count=count+1
    
average=sum/num1

print("the list elements are " + str(tempList))
print("the average of the individual elements of the list are " +str(average))
# print("the average is equal to " +str(average))  

for average in tempList:
    print(tempList)