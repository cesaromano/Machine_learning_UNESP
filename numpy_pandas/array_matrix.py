import numpy as np
#defining an array

numbers = [1, 2, 3]
a = np.array(numbers)

print(type(a))

# defining a matrix

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix = np.array(matrix)
print(matrix)

#indexing an array

print(a[0]+a[2])

#indexing a matrix

print(matrix[0, 2]+matrix[2, 2])

#slicing matrix

print(matrix[1:,0:2])