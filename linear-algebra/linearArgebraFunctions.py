# find inverse of square matrix
# usercase: in linerar regression when computing with weights using noraml equation
# allows to find original weight or solution that best fits the data
# ? the inverse of 2 is 1/2
import numpy as np

A = np.array([[1, 2],
              [4, 5]])

A_inv = np.linalg.inv(A);9

print(A @ A_inv);

# np.lin.linalg.det () -> determinant is single number that gives you info about matrice
# measure how it is invertable or scalable
print(np.linalg.det(A))
B = np.array ([[2, 5],
               [6, 8]])
print(np.linalg.det(B)) 