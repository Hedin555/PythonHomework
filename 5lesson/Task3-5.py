# к сожалению, приходится подглядывать в Ваш код (
with open('newfile2.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
    stuff = len(line)
g = 0
for i in line:
    z, x, y = i.split()
    g += int(y)
    if int(y) < 20000:
        print(f'{z} получает меньше 20 000 рублей')
print('Средняя зарплата составляет:', float(g / stuff))
