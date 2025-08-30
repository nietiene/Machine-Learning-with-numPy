# element wise-operation is the way of doing mathematical caliculation to each element in the array but individually
# ex +. -, *, /
import numpy as np

# a = [1, 2, 3]
# b = [10, 20 ,30]
# output = [1, 2, 3, 10, 20, 30]
# here it can combine array not adding them 

a = np.array([1, 2, 3])
b = np.array([10 ,20, 30])
# output = 11, 22, 33
print(a + b) 
print(b - a)
print(a * b)
print( a/ b)
print(a ** 2)

# usercase: adding bias to the element to bias in neural network + 
#  error caliculation - , multiplying values to weight * , normalization / 
# power ** is used to squaring input or plynomial features


