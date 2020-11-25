# mounth = int(input('Введите число месяца:'))
# if mounth > 12 or mounth < 1:
#     print('Всего месяцев 12')
# elif mounth >= 3 and mounth <= 5:
#     print('Весна')
# elif mounth >= 6 and mounth <= 8:
#     print('Лето')
# elif mounth >= 7 and mounth <= 11:
#     print('Осень')
# else:
#     print('Зима')

mounth = int(input('Введите число месяца:'))
user_list = ['', 'Зима', 'Зима',
             'Весна', 'Весна', 'Весна',
             'Лето', 'Лето', 'Лето',
             'Осень', 'Осень', 'Осень',
             'Зима']
if mounth > 12 or mounth < 1:
    print('Всего месяцев 12')
else:
    print(user_list[mounth])
