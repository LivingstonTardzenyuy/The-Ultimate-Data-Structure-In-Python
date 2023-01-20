myArray=[1,2,3,5,6]

temp=myArray[0]*myArray[1]
print(temp)

myNextArray=[]
for i in range(0,len(myArray)):
    for j in range(i+1,len(myArray)):
        temp=myArray[i]*myArray[j]
        # if myArray[i+1]*myArray[j+1]>temp:
        # print(temp)

        myNextArray.append(temp)

        for iterator in range(0,len(myNextArray)):
            max=iterator
            count=iterator+1
            if count+1<max:
                print("the max value is" +str(max))
                # break
            
            else:
                print("the max value is "+ str(count))
                # break
        # break
print(myNextArray)
