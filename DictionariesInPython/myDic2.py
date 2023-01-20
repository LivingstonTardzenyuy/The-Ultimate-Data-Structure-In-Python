# inputName=input("enter your name:")
# inputLevel=input("enter your current Name:")
# inputMatricule=input("enter your Matricule:")

# myDic={
#     "Name":inputName,
#     "Level":inputLevel,
#     "matricule":inputMatricule
# }

# for iterator in myDic:
#     print (iterator,myDic[iterator])


# a program to find the the missing number within a particular range which is inputed by a user

minimunValue=int(input("enter the minimume number:"))
maximumValue=int(input("entr the max value:"))

emptyArray=[]
def findTwoNumbersWhoseProductGivesANumberTheUserINput(array):
    for iterator in range(minimunValue,maximumValue):
        inputNumber=int(input("enter a number in the above range:"))

        if inputNumber<minimunValue:
            print ("the inputed number " + str(inputNumber) +" is small")
            # emptyArray.pop()
        if inputNumber>maximumValue:
            print ("the inputed number "+ str(inputNumber) + " is large")
            
        emptyArray.append(inputNumber)



    print(emptyArray)

findTwoNumbersWhoseProductGivesANumberTheUserINput(emptyArray)

def computeProductFromArray(inputedArray, usersInput):
    # max=0
    for i in range(0,len(inputedArray)):
        for j in range(i+1,len(inputedArray)):
            if inputedArray[i]*inputedArray[j]==usersInput:
                return ()
usersInput=int(input("entre a number:"))
