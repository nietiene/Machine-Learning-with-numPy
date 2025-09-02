
# ? aggregation means reducing many values into single summary value
# * example: addding all numbers together, finding maximum and minimum, computing average
# usercase in ml: summing gradient, caliculating loss, find average, reducing data dimension, 

# 1. np.sum()
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr)) # print sum of all items

# 2D array
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6]]
                 )
print(np.sum(arr2))

# loss function caliculating error (difference btn predicted value and true value)
y_true = np.array([1, 0, 1])
y_pred = np.array([0.9, 0.2, 0.8])

error = (y_true - y_pred) ** 2 # !square error to avoid negative numbers
loss = np.sum(error)
print(loss)

# 2. np.mean() computes average of numbers in the array
# formula: mean = sum of all elements / number of elements
mean = np.array([1, 2, 3 ,4, 5, 6, 7, 8])
#  1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 / 8 = 4.5
print(np.mean(mean))

# usercase: loss function use averaging error across all samples
y_true = np.array([2, -0.5, 7])
y_pred = np.array([1.8, 0.0, 8])
error = np.mean((y_true - y_pred)  **2)

print(error)
# 