import numpy as np

numbers = np.array([1, 2, 3, 4])

print(numbers.dtype)

#dtype parameter determine the array type
numbers = np.array([1, 2, 3, 0], dtype='float64')

print(numbers)

numbers = numbers.astype(np.int64)

print(numbers)

#convert number array to bool
numbers = numbers.astype(np.bool_)

print(numbers)

#convert number array to string

numbers = numbers.astype(np.string_)

print(numbers)

# convert string array to number

numbers = np.array(['0', '1', '2', '3', '4'])

print(numbers)

numbers = numbers.astype(np.int8)

print(numbers)