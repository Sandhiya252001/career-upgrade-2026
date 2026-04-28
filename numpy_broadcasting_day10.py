import numpy as np
#This is a Compatible operands(Either both the arrays should be of same size or any one array should contain size value as 1)
arr1=np.array([[1,2,3,4,5,6,7,8,9,0]])
arr2=np.array([[0],[1],[2],[3],[4],[5],[6],[7],[8],[9]])
print(arr1.shape)
print(arr2.shape)
print(arr1*arr2)
a1=np.array([[1,2,3,4],[1,2,3,4]])
a2=np.array([[2]])
print(a1*a2)



#This is not compatible
arr3=np.array([[1,2,3,4],[1,2,3,4]])
arr4=np.array([[2,5],[1,6]])
print(arr3.shape)
print(arr4.shape)
print(arr3+arr4)
print(arr3*arr4)