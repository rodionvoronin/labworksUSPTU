n = int(input())
a = []
for i in range(1, n):
    for j in range(i):
        a.append(i)
        if len(a) == n:
            break
    if len(a) == n:
        break
print(*a)