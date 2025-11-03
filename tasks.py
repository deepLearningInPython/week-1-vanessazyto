import numpy as np
#hoi
# Follow the tasks below to practice basic Python concepts.
# Write your code in between the dashed lines.
# Don't import additional packages. Numpy suffices.

# Task 1:
# Instructions:
#Write a function that takes one numeric argument as input.
#If the number is larger than zero, the function should return 1, otherwise is should return -1.
#The name of the function should be step

# Your code here:
# -----------------------------------------------

def step(number):
    if number > 0:
        return 1
    else:
        return -1

# testing
# test_1 = step(5)
# print(test_1)
# test_2 = step(-5)
# print(test_2)

# -----------------------------------------------


# Task 2:
# Instructions:
#Write a function that takes in two arguments: a numpy array, and an integer (call argument "cutoff" and set default to 0).
#The function should return a numpy array of the same length, with all elements smaller than the cutoff being set to cutoff).
#The name of the function should be ReLu


# Your code here:
# -----------------------------------------------
def ReLu(arr, cutoff = 0):
    new_array = arr.copy()
    mask = arr < cutoff
    new_array[mask] = cutoff
    return new_array

# testing
#test_3 = ReLu(arr = np.array([1,2,3,4,5,6]), cutoff = 3)
#print(test_3)


# -----------------------------------------------


# Task 3:
# Instructions:
#Write a function that takes in a two-dimensional numpy array of size (n, p) and a one-dimensional numpy array of size p.
#The function should start by multiplying the two numpy arrays (matrix multiplication).
#Next, apply the ReLu function from above to the resulting matrix and return the result.
#Name the function neural_net_layer

# Your code here:
# -----------------------------------------------

def neural_net_layer(X, y):
    multiplication = np.matmul(X, y)

    return ReLu(multiplication)


# testing
# X = np.array([
#     [1, -2, 3],
#     [0, 4, -1],
#     [2, 2, 2]
# ])
# y = np.array([1, 2, -1])
#
# #test_4 = neural_net_layer(X, y)
# print(test_4)

# ------------------------------------------

# Disclaimer: all of the functions assume that the input data types and shapes
# are as specified in the task instructions (e.g., valid numeric or NumPy arrays).
