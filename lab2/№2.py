import numpy as np

def func_a(i, j):
    return (i + 1) / (j + 1) - (j + 1) / (i + 1)
a = np.fromfunction(func_a, (10, 34))
def func_b(i, j):
    return np.exp(i) * np.tan(np.radians(j)) + np.exp(j) * np.tan(np.radians(i))
b = np.fromfunction(func_b, (34, 10))

