import numpy as np

#main numpy functions

arr = np.random.randint(0, 20, 10)

matrix = np.reshape(arr, (2, 5))

print(arr, matrix)

#obtaining the max number

print(arr.max())

#in a matrix you can give the axis to know the
#biggest number

#max row number
print(matrix.max(1))

#max colum number
print(matrix.max(0))

#getting the index where is located the max
#number in our array

print(arr.argmax(0))
print(matrix.argmax(0))

#getting the lowest number

print(arr.min())

print(matrix.min())

print(matrix.min(0))

print(matrix.argmin(1))

#getting the difference betwen the lower pick to the highest pick
# in this case: highest = 18, lowest = 1, ptp = 17

print(arr, arr.ptp())

print(matrix, matrix.ptp())

#getting ptp on each axis, we cain obtain the
#difference betwen the rows or columns in the
#matrix

print(matrix, matrix.ptp(0))

#getting the array percentile

print(arr, np.percentile(arr, 10))

#sort our array values

print(arr, arr.sort())

#getting the median, note that the percentile and
#the median are the same value

print(arr, np.percentile(arr, 50), np.median(arr))

print(matrix, np.median(matrix, 0), np.median(matrix, 1))

#getting the standard deviation

print(arr, np.std(arr))

#to get the variance just power the standard deviation

print(arr, np.std(arr)**2)

#or use the function np.var()

print(arr, np.var(arr))

#getting the mean

print(arr, np.mean(arr))

#concatenate

a = np.array([[1, 2], [3, 4]])
b = np.array([5, 6])

#as we cannot concatenate array of diferent dimentions
#we need to add a dimension to b

print(a.ndim, b.ndim)

b = np.expand_dims(b, axis=0)

print(np.concatenate((a,b), axis=0))

#transposed matrix

print(a, a.T)
print(b, b.T)