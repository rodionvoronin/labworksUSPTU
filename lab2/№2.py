import numpy as np

# создаем матрицы A и B
def func_a(i, j):
    return (i + 1) / (j + 1) - (j + 1) / (i + 1)
a = np.fromfunction(func_a, (10, 34))
def func_b(i, j):
    return np.exp(i) * np.tan(np.radians(j)) + np.exp(j) * np.tan(np.radians(i))
b = np.fromfunction(func_b, (34, 10))

#for i in range(34):
    #x = a * b[i]
#print(x)

a1 = [[1, 2, 4],
      [5, 1, 2],
      [3, -1, 1]]
b1 = [31, 29, 10]
x = np.linalg.solve(a1, b1)
print(x)