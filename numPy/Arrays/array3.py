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



# Broadcasting -> is automatically expanding aray without looping 
# If you have array with different size so broadcasting it try to expand smaller one to make sense

# rule 1: compare shapes from right to the left
# look at the size of each dimension row and column
# if they are the same works 
# if they are difference 1 it strech it
# if they are different and not 1 it fails
# shape(3, 4) and (1, 4) works
# but shape(3, 4) and (2, 4) fails

# rule 2: if the dimension is 1 expand it
# if an array has 1 numPy expand it over and over
# if first one is (3, 1) expand it to (3, 4)

# rule 3: if dimensions are missing treat them as 1 
# ex: shape 1(3, 4) shape 2 (4,)
# numPy thinks it as (1 ,4)

# example
arr = np.array([1 ,2 ,3, 4])
print(arr + 5)
# shape of arr is 4
# and shape of 5 is just one number
# so numPy predict 5 and [5, 5, 5, 5]
# so output will be [6, 7, 8, 9]
