
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
# use mean instead of sum it is easy for optimization
y_true = np.array([2, -0.5, 7])
y_pred = np.array([1.8, 0.0, 8])
error = np.mean((y_true - y_pred)  **2)

print(error)

# np.std() -> means standard deviation
# it tells us how to spread out the data is from the mean (average)
# quick recap: if all number are very close to mean means small standard deviation
# if value are spread out means large std
# usercase: Feature scarling / normalization

data = np.array([1, 3, 4, 5])
std_data = np.std(data) 
print("Standard deviation", std_data) # too small because eac numbers are very close 

# ML example
from sklearn.preprocessing import StandardScaler

data = np.array([10], [30], [50], [60])
scaler = StandardScaler()
sclaed_data = scaler.fit_transform(data)

print("Original data:\n", data.flatten())
print("Standardized Data:\n", sclaed_data.flatten())