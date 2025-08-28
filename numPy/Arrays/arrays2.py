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
# usecase in ML: Input features often has a shape (n_sample, n_features)
shapes = np.array([[1, 2, 3], [4, 5, 6]])
print(shapes.shape)

# 2. np.ndim() -> retuns dimension of array like 1D, 2D, 3D
# usercase: in ML 1D -> vector (weight, bias)
# 2D -> matrix datasets
# 3D -> tensors (images, videos, ..)

dimension = np.array([[1,2,3], [1,2,3]])
print(dimension.ndim)

# 3. np.size -> returns total number of element in the array
# usercase in ML: it tells how much datta you're handling
size = np.array([[1,2, 3, 4], [5, 6, 7, 8]])
print(size.size)