# не сложно после предыдущих задач, скорее не совсем понятно сформулировано задание
# должен ли убыток считаться в средней прибыли?

import json

with open('task7.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

my_dict = dict()
firm_profit = []
for i in lines:
    # фирма форма выручка издержки
    firm, x, revenue, costs = i.split()
    profit = int(revenue) - int(costs)
    my_dict[firm] = profit
    if profit > 0:
        firm_profit.append(profit)
av_profit = sum(firm_profit) / len(firm_profit)
new_dict = [my_dict, {'средняя прибыль': av_profit}]
print(new_dict)

with open('task7.json', 'w', encoding='utf-8') as k:
    json.dump(new_dict, k)
