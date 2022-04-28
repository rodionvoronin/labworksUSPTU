from math import *
a = int(input('Коэффициент 1: '))
b = int(input('Коэффициент 2: '))
c = int(input('Коэффициент 3: '))
discriminant = b ** 2 - 4 * a * c
if discriminant < 0:
    print('Нет корней', f'D={discriminant}', sep='\n')
elif discriminant == 0:
    x = - b / 2 / a
    print(f'Корень: {x}')
else:
    x1 = (- b - sqrt(discriminant)) / (2 * a)
    x2 = (- b + sqrt(discriminant)) / (2 * a)
    print(f'Корень 1: {x1}', f'Корень 2: {x2}', sep='\n')