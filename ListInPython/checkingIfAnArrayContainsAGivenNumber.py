number=int(input("enter a given number to search:"))

def findNumber(array,num):
    for i in range(0,len(array)):
        if(array[i]==num):
            print("the number if found in index " + str(i))

numbers=[1,5,7,4,6,4,6]
findNumber(numbers,number)