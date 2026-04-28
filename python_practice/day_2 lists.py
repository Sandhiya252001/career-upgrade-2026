#Find Largest Number
numbers = [12,34,72,44,92,56]
largest = max(numbers)
print("Largest number : ", largest)

#Sum of list
num=[1,2,3,4,5,6]
total=sum(num)
print("The sum of numbers : ", total)

#Second highest value
arr=[2,4,5,6,7]
arr=list(set(arr)) # Remove duplicates
arr.remove(max(arr)) # Remove highest 
print(max(arr))

x=2
y=2
z=2
n=2
result=[]
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k != n:
                result.append([i,j,k])
print(result)
         
