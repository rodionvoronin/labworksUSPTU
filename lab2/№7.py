from sympy import *

x, y, z = symbols('x y z') 
eq_1 = Eq(x + 2*y + 4*z - 31, 0) 
eq_2 = Eq(5*x - y - 2*z - 29, 0)
eq_3 = Eq(3*x - y + z - 10, 0) 
print(linsolve([eq_1, eq_2, eq_3], [x, y, z]))