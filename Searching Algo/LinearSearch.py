
#created by kongnyuy on 17/02/2023

def LinearSearch(list, target):
    for i in range(0, len(list)):
        if list[i]==target:
            return i
        None

def verify(index):
    if index is not None:
        print("target found at index", index)
    else:
        print("no value found")

tempList=[10,20,30,40,50,60,70,80,90]
verify=LinearSearch(tempList, 800)
print(verify)