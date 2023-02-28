#created by kongnyuy livingstone on 26/02/2023

def merge_sort(list):
    if len(list)<=1:
        return list
    else:
        left_half, right_half= split(list)
        left=merge_sort(left_half)
        right=merge_sort(right_half)

    return merge(left, right)

#implimenting the split operation

def split(list):
    midpoint=len(list)//2
    # using slizing
    left=list[:midpoint]
    right=list[midpoint:]

    return left, right

#merging and sorting
def merge(left, right):
    newList=[]
    i=0
    j=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            newList.append([i])
            i+=1
        else:
            newList.append([j])
            j+=1

    return newList
    #when the right loop is smaller than the left
    while i<len(left):
        newList.append([i])

    while j<len(right):
        newList.append([j])
mylist=[6,7,3,1,0,-4,90,5]
l=merge_sort(mylist)
print(l)