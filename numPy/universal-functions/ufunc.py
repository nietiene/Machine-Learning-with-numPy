# universal function(ufuncs) is function that operate wise-element on darrays
# * they are fast and applied to the whole array at once
# * ex: np.add, np.subtract, np.exp, np.log, np.sqrt etc...

# 1. np.exp() -> computes an exponential of each element in the input array
# where e = 2.718 (Euler's number)
# usercase: softmax function  convert secores into probabilities
import numpy as np

# single value 
print(np.exp(1)) # e^1
print(np.exp(2)) # e^2

# array of numbers
array = np.array([1, 2, 3, 4, 5])
print(np.exp(array)) # apply exponential to each item in the array

score = np.array([2.0, 5.0, 6.0])
exp_secore = np.exp(score) # to male all number positive becuase probability can not be less than 0
probabilites = exp_secore / sum(score)
print(probabilites)