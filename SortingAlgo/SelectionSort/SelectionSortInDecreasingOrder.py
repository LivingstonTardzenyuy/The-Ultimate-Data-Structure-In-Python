def selectionSort(array):
    for i in range(len(array)-1):
        min = i
        for j in range(i+1, len(array)):
            if array[j]>array[min]:
                array[j],array[min]=array[min],array[j]
    print(array)
list=[9,3,6,99,4,1,2]
selectionSort(list)