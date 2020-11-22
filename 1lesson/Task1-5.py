
print('Данные вводятся с округление до целых')
proceeds = int(input('Введите сумму выручки за прошедший год: '))
costs = int(input('Введите сумму издержек за прошедший год: '))
profit = (proceeds - costs)
if proceeds > costs:
    print('Компания прибыльна')
    print(f'Рентабельность выручки составляет: {int(profit)}')
    employees = int(input('Введите количество сотрудников: '))
    print(f'Прибыль компании на одного сотрудника составляет: {int(profit / employees)}')
else:
    print('Компания не приносит прибыли, значение составляет:', profit)
