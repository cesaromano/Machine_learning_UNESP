import numpy as np

#creating an array

array = np.arange(0, 10, 2)

print(array)

#create a zero array
#creating a zero array is quite usefull to
#create a tensor esqueme

zeroa = np.zeros(5)

print(zeroa)

#create a matrix array

zerom = np.zeros((5, 5))

print(zerom)

#create an array with ones

onesa = np.ones((5, 5))

print(onesa)

#np.linspace() function creates an array distributed
#(lower range, upper range, number of data)

distribution = np.linspace(0, 10, 20)

print(distribution)

#creating a diagonal matrix whit ones

diagmatrix = np.eye(4)
print(diagmatrix)

#generating random numbers

randomval = np.random.rand()

print(randomval)

#generatin a random array

randomarr = np.random.rand(6)

print(randomarr)

#generating a random matrix

randomat = np.random.rand(6, 6)

print(randomat)

#int random values

randval = np.random.randint(1, 15)

print(randval)

#int random matrix

randmat = np.random.randint(1, 15, (10, 10))

print(randmat)