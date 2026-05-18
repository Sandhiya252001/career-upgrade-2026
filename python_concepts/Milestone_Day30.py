#1. Lists - Ordered, Mutable, Allow duplicates
a=[1,2,3,4]
print(a[1])
#List enumerate
for i in enumerate(a):
    print(i)
a.append(5)
print(a)
#Insert - to add in specific index
a.insert(2,0)
print(a)
#List operations = append, insert, pop, remove,del,clear()

#2..Tuples - ordered, immutable,allows duplicates
b=(1,2,3,4,9,10)
print(type(b))
print(len(b))

#3.Set - unordered,immutable,doesnt allow duplicates
c=set(b)
d={1,2,3,4,5}
print(c)
d.add(6)
d.remove(3)
#set operations = union:| , intersection : & , differance : -, semantic : ^
print(d)
print(c|d)
print(c&d)
print(c-d)
print(c^d)

#4.Dictionary - ordered, mutable, dont allow duplicates
dic={"x":2,"y":2}
print(dic["x"])
if "a" in dic:
    print(dic["a"])
print(dic.get("a",0))

#5 Function
def add(a,b):
    a=a
    b=b
    return a+b
a=add(1,2)
print(a)

#6 *args(for tuple) and **kargs(for dictionary)
def add(*nums):
    total=0
    for i in nums:
        total+=i
    return(total)
print(add(1,2,4,7))
def printAddress(**data):
    for key,value in data.items():
        print(f"{key}:{value}")
printAddress(street="ABC",
             apt="100",
             state="TN")

#Lambda
double=lambda x:x*2
sum= lambda x,y:x+y
print(double(4),sum(5,6))

#7 Map/Filter
n=[1,2,3,5,8,90,23,58,7]
even=list(filter(lambda x:x%2==0,n))
doubles=list(map(lambda y : y*2,n))
print(even)
print(doubles)

#8 List Comprehensions:
squares = [i*i for i in n]
print(squares)





