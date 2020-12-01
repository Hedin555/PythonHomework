# def my_func(x, y):
#     answer = x ** y
#     return answer


# print(my_func(2, -2))

# списано

def my_func(x, y):
    x, y = float(x), int(y)
    res = x
    for i in range(abs(y) - 1):
        res = res * x
    return 1 / res


x = float(input('Введите положительное число: '))
y = int(input('Введите целое отрицательное число: '))
print(my_func(x, y))
