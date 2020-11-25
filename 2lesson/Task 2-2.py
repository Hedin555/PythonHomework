# Не понял решения, если честно, списано....
user_list = list(input('Введите любой текст:'))
for a in range(1, len(user_list), 2):
    user_list[a - 1], user_list[a] = user_list[a], user_list[a - 1]
print(user_list)
