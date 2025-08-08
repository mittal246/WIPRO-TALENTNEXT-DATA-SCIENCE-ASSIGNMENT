#1. Create two-dimensional 3*3 array and perform ndim,shape,slicing operation on it.
import numpy as np

# 1. Create a 2D 3x3 array
arr_2d = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

print("2D Array:\n", arr_2d)

# ndim (number of dimensions)
print("ndim of arr_2d:", arr_2d.ndim)

# shape (rows, columns)
print("shape of arr_2d:", arr_2d.shape)

# slicing operation
print("First two rows:\n", arr_2d[:2])
print("First two columns:\n", arr_2d[:, :2])
print("Element at row 2, col 3:", arr_2d[1, 2])

#2. Create one dimensional array and perform ndim,shape,reshape operation on it.
arr_1d = np.array([10, 20, 30, 40, 50, 60])

print("1D Array:", arr_1d)

# ndim
print("ndim of arr_1d:", arr_1d.ndim)

# shape
print("shape of arr_1d:", arr_1d.shape)

# reshape into 2x3 array
reshaped_arr = arr_1d.reshape(2, 3)
print("Reshaped (2x3) array:\n", reshaped_arr)
