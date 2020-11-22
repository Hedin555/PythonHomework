# Не решил сам, списал у Вас :_( голова пока не работает в эту сторону
user_n = int(input('Введите целое положительное число: '))
max_n = 0
num = user_n
while num > 0:
    digit = num % 10
    if digit > max_n:
        max_n = digit
    num = num // 10
print(f'Максимальной цифрой в числе {user_n} является {max_n}')