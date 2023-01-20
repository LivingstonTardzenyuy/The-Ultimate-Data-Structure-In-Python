#cancetination
num1=[1,2,3,4,5,6]
num2=[7,8,9,0]
c=num1+num2
print(c)

#duplication
num3=[4,5,7]
num3=num3*3
print(num3)

print(max(num1))
print(min(num1))

print((max(num1)+min(num1))/2)
print(sum(num1)/len(num1))

def average():
    total=0
    count=0
    while(True):
        inp=input("Enter a number:")
        if(inp!='done'):
            inp=float(inp)
            total+=inp
            count+=1
        else:
            result=total/count
            return(result)
print("The average of the number is")
print(average())