# find inverse of square matrix
# usercase: in linerar regression when computing with weights using noraml equation
# ? the inverse of 2 is 1/2
import numpy as np

A = np.array([[1, 2],
              [4, 5]])

A_inv = np.linalg.inv(A);

print(A @ A_inv);

