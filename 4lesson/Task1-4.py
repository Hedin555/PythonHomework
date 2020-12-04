from sys import argv

if 'h' in argv:
    print('h - help, с - calculation of wages')
elif 'c' in argv:
     x = float(input('Введите стоимость часа работника\n'))
     y = int(input('Введите выработку работника в часах\n'))
     z = float(input('Введите сумму премии работника\n'))
     print('Зарплата работника за день составила:', x * y + z)
else:
    print('End programm')
