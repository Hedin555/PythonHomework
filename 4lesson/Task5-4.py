import functools
def my_f(x, y):
    return x + y

my_list = [x for x in range(100, 1000) if x % 2 == 0]
print(f'{my_list}\n {functools.reduce(my_f, my_list)}')

