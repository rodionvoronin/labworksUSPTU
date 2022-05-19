from sympy import *

f = symbols('f', cls=Function)
x = symbols('x')
diff_eq = Eq(
3*f(x) – 4*f(x).diff(x) + f(x).diff(x, x),
0
)
solution = dsolve(diff_eq, f(x))
print(solution)

diff_eq = Eq(
3*f(x) – 4*f(x).diff(x) + f(x).diff(x, x),
sin(x)
)
solution = dsolve(diff_eq, f(x))
print(solution)
