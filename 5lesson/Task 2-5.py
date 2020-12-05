# к сожалению, приходится подглядывать в Ваш код (
with open('newfile1.txt', 'r') as f:
    context = f.readlines()
for x, i in enumerate(context, start=1):
    print(f'Строка: {x}, Текст: {i.strip()}, Слов: {len(i.split())}')
