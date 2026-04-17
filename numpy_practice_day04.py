#2D array and reshaping
import numpy as np
from numpy import matrix
a=np.array([[1,2,3,0],[4,5,6,3],[7,8,9,5]])
print(a) #prints a 2D array
print(a.flatten()) # converts 2D to 1D array
print(a.reshape(4,3))
print(a.reshape(6,2))
print(a.reshape(-1,1))
print(a.reshape(1,-1))
print(a.reshape(3,2,2)) # prints 3(2 dimensional array) in one big array, each 2 dimensional array has 2 one dimensinal array and each one dimensional array has 2 values
a1=np.array([[1,2,3,4,5,0],[6,7,8,9,0,3],[11,12,13,14,15,1],[16,17,18,19,4,22]])
print(a1.reshape(4,3,2))

#Matrix Operations
m=matrix('1 2 3 4;5 6 7 8;9 10 11 12')
print(m)
print(m.diagonal()) # prints only diagonal values
print(m.min()) # prints minimum value
print(m.max()) # prints maximum value

m1=matrix('1 3 6;7 9 11;5 3 9')
m2=matrix('2 4 1;6 7 8;2 4 7')
m3=m1+m2
m4=m1*m2
print(m3)
print(m4)