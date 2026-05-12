import numpy as np
a=np.array([1,2,3,4])
#view
a1=a.view()
print(f"original array a :{a}")
print(f"original array a :{a1}")
a[0]=20
print(f"changed array a :{a}")
print(f"changed array a :{a1}")
#copy
b=np.array([7,8,9,0])
b1=b.copy()
print(f"original array a :{b}")
print(f"original array a :{b1}")
b[3]=10
print(f"changed array a :{b}")
print(f"changed array a :{b1}")