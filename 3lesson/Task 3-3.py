def my_func(x, y, z):
    my_list = [x, y, z]
    result_list = my_list.copy()
    result_list.sort(reverse = True)
    result_list.pop()
    return sum(result_list)


print(my_func(1, 5, 3))
