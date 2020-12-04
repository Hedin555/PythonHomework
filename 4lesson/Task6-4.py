import itertools
import time

# part 1
for el in itertools.count(start=int(input('Введите целое число: ')), step=1):
    print(el)
    if el >= 20:
        break

# part 2
my_list = ['red', 'orange', 'green']
start = time.time()
for x in itertools.cycle(my_list):
    time.sleep(1)
    print(x)
    end = time.time()
    if end - start > 10:
        break
