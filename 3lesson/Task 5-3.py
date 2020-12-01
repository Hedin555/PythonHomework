
# списано

def my_func():
    x = False
    while x == False:
        numbers = input('Введите число или q для выхода: ').split()
        res = 0
        for num in numbers:
            if 'q' in num:
                x = True
                break
            res += int(num)
        result += res
    return result


