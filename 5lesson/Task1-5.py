with open('newfile.txt', 'w', encoding='utf-8') as f:
    while True:
        text = input('Введите текст: ')
        if text == '':
            break
        f.write(text + '\n')
