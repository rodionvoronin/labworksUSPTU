number = int(input())
summ = 0
while number != 0:
    summ += number
    number = int(input())
if summ == 0:
    print(summ)
else:
    print(f'Сумма: {summ}')