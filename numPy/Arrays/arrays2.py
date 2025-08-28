# Array initialization

import numpy as np

# 1 np.zeros(row, colums) -> is used to initialize array with zero value
# produce array which has zero values 
# usercase: in ML is used to initialize weight to zero value in neular network
# represent empy array before filling data
zero = np.zeros((2, 3))
print(zero)

# 2. np.ones(rows, colums) -> create array field with ones
# usercaes: initialize bias in neural networks, quick testing algorithm
ones = np.ones((2, 3) , dtype=int)
print(ones)


# 3 np.eye() -> is used to create indentical matrix
# usercase: linear algebra used in ML optimization
# solving system equations
matrix = np.eye((4))
print(matrix)

# arrays attributes
# 1. np.shape -> returns dimensions of arrays as turple, returns rows and columns as turple (rows, colums)
# usecase in ML: Input features often has a shape (n_sample, n_features), checks if matrix are compatible for mulitiplication
shapes = np.array([[1, 2, 3], [4, 5, 6]])
print(shapes.shape)

# 2. np.ndim() -> retuns dimension of array like 1D, 2D, 3D
# usercase: in ML 1D -> vector (weight, bias), ensure if your model input is correct
# 2D -> matrix datasets
# 3D -> tensors (images, videos, ..)

dimension = np.array([[1,2,3], [1,2,3]])
print(dimension.ndim)

# 3. np.size -> returns total number of element in the array
# usercase in ML: it tells how much datta you're handling
size = np.array([[1,2, 3, 4], [5, 6, 7, 8]])
print(size.size)

# 4. np.dtype -> returns data type of the elements in the array
# usercase: ensure your data and weight is in the right type
datatype = np.array([1,2, 3], dtype=float)
print(datatype.dtype)

# Indexing and slicing 
# 1. indexing -> choosing specific elements in the array
# 1D example
array = [10, 20 ,30, 40, 50]
# indexing
print(array[0]) # first element
print(array[-1]) # last element

# slicing
print(array[0:3]) # from index 0 up to index 3
print(array[:3]) # include first three elements
print(array[::3]) # include first second element  jump every items on thrid index

# 2D example
# indexing
array2 = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(array2[0, 0]) # row on index 0 and col on index 0

# slicing
print(array2[0, :]) # row 0 and all colums
print(array2[:, 0]) # all rows colum 0
print(array2[1, 1])