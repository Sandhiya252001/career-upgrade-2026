#1.Printing numbers 1 to 10
for number in range(1,11):
    print(number)

#2.Printing even numbers

count =0
for num in range(1,10):
    if(num%2==0):
        count+=1
        print(num)
print(f"we have {count} even numbers")

#3.Sum of Numbers
total=0
for a in range(1,5):
    total=a+total
print(f"The sum of numbers is {total}")


#4.Nested While
i = 1
while i <= 5:
    print("hello", end="")
    
    j = 1
    while j <= 3:
        print(".", end="")
        j = j + 1   # important
    
    print()
    i = i + 1      # important



