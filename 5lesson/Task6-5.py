# списано, но понятно
with open('task6.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

my_dict = dict()
for i in lines:
    line = i.split()
    subject = line[0]
    sum_l = sum([int(x[:x.find('(')]) for x in line[1:] if '(' in x])
    my_dict[subject[:-1]] = sum_l
print(my_dict)