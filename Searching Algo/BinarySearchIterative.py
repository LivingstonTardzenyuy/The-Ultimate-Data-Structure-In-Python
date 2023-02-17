#created by kongnyuy on 17/02/2023

def binarySearch(list, target):
    first=0
    last=len(list)-1


    while first<=last:
        midvalue = (first + last) // 2
        if list[midvalue]==target:
            return midvalue

        elif list[midvalue]<target:
            first=midvalue+1

        else:
            last=midvalue-1

    return None

tempList=[10,20,30,40,50,60,70,80,90]
print(binarySearch(tempList,80))