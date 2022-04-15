import numpy as np

#matrix is composed by columns(atributes) and rows(instances)

#tensor is composed by columns(atributes), rows(time or serie) and examples

#tensor 4D images, columns(height), rows(weight), chanels and examples

scalar = np.array(56)

#print dimension number
print(f"Dimension number: {scalar.ndim}")

vector = np.array([1, 2, 3, 4, 5])

print(f"Dimension number: {vector.ndim}")

matrix = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(f"Dimension number: {matrix.ndim}")

tensor = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]])

print(f"Dimension number: {tensor.ndim}")

#Adding or deleting dimensions when dfining array

vector = np.array([1, 2, 3], ndmin=10)
print(vector)
print(f"Dimension number: {vector.ndim}")

#parameter axis=1, 0 defines if dimension is added to the row or column
# np.expand_dims(array, axis to expand)

expanded = np.expand_dims(np.array([1, 2, 3]), axis=1)
print(expanded)
print(expanded.ndim)

#to delete dimensions aren't used

print(vector, vector.ndim)
vector2 = np.squeeze(vector)
print(vector2, vector2.ndim)

#creating a 5 dimensions tensor

tensor5 = np.array([1], ndmin=5)
print(tensor5, tensor5.ndim)