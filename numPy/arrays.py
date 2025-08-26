import numpy as np

# np.arrays is function which helps to create arrays in numPy
# 1D Array think like single feature in ML
a = np.array([1, 2, 3])
print(a) # print value of a
print(type(a)) # print type of a ndarray
print(a.shape) # print shape of a  3 

# 2D arrays used to represent Dataset, with rows = samples and colums = features 
b = np.array([[1, 2, 3],
             [4, 5, 6]])
print(b)
print(b.shape)