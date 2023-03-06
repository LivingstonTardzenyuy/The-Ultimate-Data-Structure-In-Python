import math
def bucketSort(array):
    square=math.sqrt(len(array))
    numberOfBuckets=round(square)
    maxValue=max(array)

    arr=[]
    for i in range(numberOfBuckets):
        arr.append([])
    for j in array:
        index_of=math.ceil(j*numberOfBuckets/maxValue)
        arr[index_of-1].append(j)

    for i in range(numberOfBuckets):
        for j in range(array[i]):
            if array[j]<array[j+1]:
                array[j],array[j+1]=array[j+1], array[j]
    print(array)

    k=0
    for i in range(numberOfBuckets):
        for j in range(len(arr[i])):
            array[k]=arr[i][j]
            k+=1
list=[9,3,6,99,4,1,2,44,6,2,-4,-6,-2]
bucketSort(list)
