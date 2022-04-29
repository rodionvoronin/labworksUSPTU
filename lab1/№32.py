from random import *

z = int(input('Кол-во студентов: '))
m = int(input('Кол-во задач: '))
n = int(input('Кол-во задач на дом: '))

tasks = [str(i) for i in range(1, m + 1)]

st1 = sample(tasks, n)
print('Студент 1:', ', '.join(st1))

for i in range(2, z + 1):
    st = sample(tasks, n)
    while set(st1) == set(st):
        st1 = sample(tasks, n)
        st = sample(tasks, n)
        continue
    print(f'Студент {i}:', ', '.join(st))
