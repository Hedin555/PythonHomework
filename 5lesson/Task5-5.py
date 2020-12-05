with open('task5.txt', 'w', encoding='utf-8') as f:
    text = input('Введи целые числа через пробел: ')
    f.write(text)

with open('task5.txt', 'r', encoding='utf-8') as f:
    (context) = f.readlines()

g = 0
my_list = context[0].split()
for i in my_list:
    g += int(i)
print(g)
