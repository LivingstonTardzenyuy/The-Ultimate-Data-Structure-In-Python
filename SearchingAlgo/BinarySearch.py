import math
def BinarySearch(InputArray,target):
    min=InputArray[0]
    max=InputArray[19]
    print(max)
    print(min)
    mid=math.floor((min+max)/2)
    if target==mid:
        return target
    elif targer>mid:
        min=inputArray[target+1]
        return target
    else:
        max=inputArray[target-1]
        return target
        
temptarget=int(input("enter a value to search between 1 to 20:"))
array=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,15,16,17,18,19,20]
BinarySearch(array,temptarget)
