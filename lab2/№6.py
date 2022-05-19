from sympy import *
init_printing(use_unicode=True,
              wrap_line=True,
              no_global=True)
x, y, z = symbols('x y z')
eq_1 = Eq(z, x/y - y/x)
print(solveset(eq_1, x))

eq_1 = Eq(y, x**2 - x**5 + 1)
eq_2 = Eq(y, x**3 + x**7)
print(solveset(eq_1, eq_2))

print(integrate(x**2 - x**5 + 1, x))
print(integrate(x**3 + x**7, x))
print(integrate(x/y - y/x, x, y))

print(diff(x**2 - x**5 + 1, x))
print(diff(x**3 + x**7, x))
print(diff(x/y - y/x, x, y))
