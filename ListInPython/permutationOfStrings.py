# def findMissingNumber(arr):
#     for i in range(0,len(arr)):
#         if arr[i+1]-arr[i]==1:
#             if i==len(arr)==1:
#                 break
            
#         else:
#             num=arr[i]+1
#             print(num)
# array=[1,2,3,4,5,7,8,9,10]

# findMissingNumber(array)

# def addPairsOfIntegers(arr,n):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j]==n:
#                 print("the user found the element which are " + str(arr[i] ) + str(arr[j]))
                
#             else:
#                 return ("the numbers does not exist")

# array=[1,2,3,4,5,7,8,9,10]

# number=int(input("enter the number to find: "))

# addPairsOfIntegers(array,number)

# def findMaxElementInAnArray(arr):
#     product=0
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]*arr[j]>product:
#                 # return ("the max elements are" + str(arr[i+1]) +str(arr[j+1]))
#                 product=arr[i]*arr[j]

#     print(product)
# array=[1,2,3,4,5,7,8,9,10]



# findMaxElementInAnArray(array)
