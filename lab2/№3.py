import numpy as np

#задание 1
coeff1 = [-1, 0, 0, 1, 0, 1]
coeff2 = [1, 0, 0, 0, 1, 0, 0, 0]
a = np.roots(coeff1)
b = np.roots(coeff2)
print(np.float64(a[0]))
print(np.int64(b[4]))

#задание 2
coeff = [1, 0, 1, 0, 1, -1, 0, -1]
c = np.roots(coeff)
for i in c:
    print(i)