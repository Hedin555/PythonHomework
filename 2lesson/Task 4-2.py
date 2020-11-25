text = input('Введите текст:')
text_new = text.split()
for a, b in enumerate(text_new, start=1):
    print(a, b)
