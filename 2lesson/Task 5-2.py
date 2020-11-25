my_list = [8, 6, 4, 3, 1]
reit_user = int(input('Введите рейтинг:'))
result_list = my_list.copy()
result_list.append(reit_user)
result_list.sort(reverse=True)
print('Первоначальный список', my_list)
print('Новый список', result_list)
