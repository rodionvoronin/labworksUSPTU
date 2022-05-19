from scipy.integrate import quad
import numpy as np
func = lambda x: 5**x - 6 / (9 - x**2) + 2*np.cosh(x)
solution = quad(func, -100, 100)
print(solution)