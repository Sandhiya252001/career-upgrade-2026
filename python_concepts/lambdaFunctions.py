double=lambda x:x*2
print(double(6))
is_even=lambda a:a%2==0
print(is_even(6))
greater_num=lambda a,b:a if a>b else b
print(greater_num(6,7))
data=[1,4,10,6,11,20,8]
data.sort()
print(data)
data=[(1,7),(4,5),(2,2),(8,1)]
data.sort(key=lambda x:x[0])
print(data)