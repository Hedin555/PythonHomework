def my_func(x, y):

    try:
        x = float(x)
        y = float(y)
        answer = x / y
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    return answer


x = float(input('Введите x '))
y = float(input('Введите y '))
total = round(my_func(x, y), 2)
print(total)
