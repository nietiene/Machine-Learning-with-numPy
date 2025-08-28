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