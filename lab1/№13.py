from datetime import *

b_date = [int(i) for i in input('Дата заказа: ').split('.')] 
booking_date = date(b_date[0], b_date[1], b_date[2])
delta = timedelta(int(input('Количество дней брони: ')))
wedding_date = str(booking_date + delta)

print(wedding_date.replace('-', '.'))
