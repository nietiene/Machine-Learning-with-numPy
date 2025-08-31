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

# simple softmax function
score = np.array([2.0, 5.0, 6.0])
exp_secore = np.exp(score) # to male all number positive becuase probability can not be less than 0
probabilites = exp_secore / np.sum(np.exp(score))
print(probabilites)

# Gradient Descent
# row output of model
# usercase: image classification, text calassification, 
scores = np.array([1000, 1001, 1002])
# the why we shifted by max is to make numbers smaller which is better for computation
shifted_scores = scores - max(scores)
# make all numbers positive
exp_secores = np.exp(shifted_scores)
# find probabilities
probs = exp_secores / np.sum(exp_secores);

print(probs)