import numpy as np

# create vector
vector = np.array([1, 2, 3, 4, 5])

# create vector with range
vector_range = np.arange(1, 6,  2)

# create linspace
vector_linspace = np.linspace(1, 6, 3)

# create zeros
vector_zeros = np.zeros(5)
matrix_zeros = np.zeros((3, 3))

# create array multi-dimension
matrix_array = np.array([[1, 2], [3, 4], [5, 6]])

# create matrix with ones
matrix_ones = np.ones((3, 3))

# create matrix identity
matrix_identity = np.eye(3)

# display
print("vector = ", vector)
print("vector_range = ", vector_range)
print("vector_linspace = ", vector_linspace)
print("vector_zeros = ", vector_zeros)
print("matrix_zeros = \n",  matrix_zeros)
print("matrix_array = \n", matrix_array)
print("matrix_ones = \n", matrix_ones)
print("matrix_identity = \n", matrix_identity)