import numpy as np
arr=np.random.randint(low=1,high=100,size=20).reshape(4,5)
print(arr)
result=arr>50
print(result)
r=arr[arr>50]
print(r)
R=arr[(arr>50) & (arr%2!=0)]
print(R)
arr[(arr>50) & (arr%2!=0)]=0
print(arr)