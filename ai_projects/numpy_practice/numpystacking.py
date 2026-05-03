import numpy as np
arr1=np.array([1,2,3,4])
arr2=np.array([4,5,6,7])
result=np.stack([arr1,arr2],axis=0)
result1=np.stack([arr1,arr2],axis=1)
print(f"{result,result1}")
print(result.shape)
print(result1.shape)