import numpy as np
from numpy.random import Generator as gen
from numpy.random import PCG64 as pcg
arr=gen(pcg(seed=100))
print(arr.normal(size=(5,5))) # bell curve
print(arr.integers(low=10,high=99,size=(3,3)))
print(arr.random(size=(6,4)))