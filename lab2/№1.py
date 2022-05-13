import numpy as np
from numpy.linalg import matrix_power

def func_a(i, j):
    return (i + 1) / (j + 1) - (j + 1) / (i + 1)
a = np.fromfunction(func_a, (10, 34))
def func_b(i, j):
    return np.exp(i) * np.tan(np.radians(j)) + np.exp(j) * np.tan(np.radians(i))
b = np.fromfunction(func_b, (34, 10))

print(np.transpose(a))
print(np.transpose(b))
# print(a + b)
# print(a - b)
print(np.dot(a, b))
print(np.dot(b, a))
# print(np.divide(a, b))
# print(np.divide(b, a))
# A = matrix_power(a, -1) print(A)
# B = matrix_power(b, -1) print(B)
# print(np.dot(a, B))
# print(np.dot(b, A))
one = np.eye(34, 10)
print(2 * np.transpose(a) - one)
# polynomial_A = matrix_power(a, 3) - 7 * matrix_power(a, 2) + 13 * a - 5
# polynomial_B = matrix_power(b, 3) - 7 * matrix_power(b, 2) + 13 * b - 5
# function1_A = matrix_power(a, 2) - matrix_power(a, 5) + 1
# function1_B = matrix_power(b, 2) - matrix_power(b, 5) + 1
# z = np.divide(b, a) - np.divide(a, b)