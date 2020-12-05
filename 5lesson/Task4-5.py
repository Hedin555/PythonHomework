# списал по сути
with open('task4.txt', 'r') as f:
    line = f.readlines()

with open('task41.txt', 'w', encoding='utf-8') as f:
    for i in line:
        x, z, y = i.split()
        if x == 'One':
            x = 'Один'
            f.write( x + ' - ' + y + '\n')
        if x == 'Two':
            x = 'Два'
            f.write( x + ' - ' + y + '\n')
        if x == 'Three':
            x = 'Три'
            f.write(x + ' - ' + y + '\n')
        if  x == 'Four':
            x = 'Четыре'
            f.write(x + ' - ' + y + '\n')