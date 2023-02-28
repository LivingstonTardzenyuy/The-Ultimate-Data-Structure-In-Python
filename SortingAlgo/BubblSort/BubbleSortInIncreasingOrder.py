def list():
    maxsize=int(input("enter the maxsize: "))
    mylist=[]
    i=0
    while i<maxsize:
        mylist.append(i)
        i+=1
        
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1], array[j]

    print(array)
list=[9,3,6,99,4,1,2]
bubbleSort(list)

