#created by kongnyuy livingston 

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j>=0 and key < array[j]:
            array[j+1] = array[j]
            j-=1
        array[j+1] = key
    print(array)
list=[9,3,6,99,4,1,2,44,6,2,-4,-6,-2]
# print('l')
insertionSort(list)