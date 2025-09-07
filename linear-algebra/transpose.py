import numpy as np
# transpose -> is to transpose matrice by swaps its row and column (row become column and column become row)
# only affect 2D array
# ? usercase: is used to align shapes correctly 

A = np.array([[1, 2,],
              [3, 4]])

print("Original: ", A)

print("Transposed: ", A.T)
