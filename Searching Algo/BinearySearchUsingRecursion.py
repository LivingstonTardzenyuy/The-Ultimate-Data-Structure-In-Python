#created by kongnyuy livingston

def BinaryUsingRecursion(list, target):
    if len(list)==0:
        return False
    else:
        midvalue=len(list)//2
        if list[midvalue]==target:
            return True

        elif list[midvalue]<target:
            return BinaryUsingRecursion(list[midvalue+1:], target)

        return BinaryUsingRecursion(list[:midvalue-1], target)

tempList=[10,20,30,40,50,60,70,80,90]
print(BinaryUsingRecursion(tempList,60))



