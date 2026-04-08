#Fizz Buzz
def fizz_buzz(input):
    if input%3==0 and input%7==0:
        result="Fizz Buzz"
        #Alternate easy way : 
        #return"Fizz_Buzz
    elif input%7 ==0:
        result="Buzz"
    elif input%3==0:
        result="Fizz"
    elif input%3!=0 or input%7!=0:
        result=input
    return result
print(fizz_buzz(10))  

#Function to find square
def find_square(value):
    return value*value
print(find_square(4))

#Function to check even or odd
def odd_even(number):
    if number%2==0:
        return "even"
    return "odd"
print(odd_even(6))

#Function to find largest of three numbers
def find_largest(a,b,c):
    # if(a>b and a>c):
    #     return "A is Greatest"
    # if(b>a and b>c):
    #     return "B is Greatest"
    # if(c>a and c>b):
    #     return "C is Greatest"
    
    #ALternate way
    return max(a,b,c)
print(find_largest(22,6,10))

#Arithmetic Operators
a = int(input())
b = int(input())
def arith_ops():
    c=a+b
    print(c)
    d=a-b
    print(d)
    e=a*b
    print(e)
    
print (arith_ops())

#Python division
x=int(input())
y=int(input())
print(x//y)
print(x/y)


     