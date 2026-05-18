import numpy as np
a=np.array(([1,2,3]),dtype='int16')
b=np.array([[10.0,20.0,30.0],[40.0,50.0,60.0]])
#printing arrays
print(a)
print(b)
#get dimensions of array
print(a.ndim)
print(b.ndim)
#get shape of an array
print(a.shape)
print(b.shape)
#get type of the array elements
print(a.dtype)
print(b.dtype)
#get byte size 
print(a.size)
print(b.size)
#get size/len of array
print(a.itemsize)
print(b.itemsize)
#get no of bytes
print(a.nbytes)
print(b.nbytes)
