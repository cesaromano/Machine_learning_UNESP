import numpy as np

#shape gives the shape o an array

arr = np.random.randint(0, 11, (4, 5))

print(arr, arr.shape)

#reshape arrange the array in a especific way
#you cannot change the shape if it doesn't respect
#the number os elements

reshaped = arr.reshape(2, 10)

print(reshaped)

reshaped = arr.reshape(10, 2)

print(reshaped)

reshaped = np.reshape(arr, (20, 1))

print(reshaped)

#reshape using diferent orders:
#C = C code based
#F = Fortran code based
#A = optimized based, usually the same as C 

reshaped = np.reshape(arr, (2, 10), 'C')

print(reshaped)

reshaped = np.reshape(arr, (2, 10), 'F')

print(reshaped)

reshaped = np.reshape(arr, (2, 10), 'A')

print(reshaped)