# увы, но во всю подглядывал - идет со скрипом.
class Cell:
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return 'Сумма клеток ' + str(self.num + other.num)

    def __sub__(self, other):
        if self.num - other.num < 0:
            return 'Вычитание невозможно'
        else:
            return self.num - other.num

    def __mul__(self, other):
        return 'Умножение клеток ' + str(self.num * other.num)

    def __truediv__(self, other):
        return 'Деление клеток ' + str(self.num / other.num)

    def make_order(self, x):
        return '\n'.join(['*' * x for _ in range(self.num // x)]) + '\n' + '*' * (self.num % x)


cell1 = Cell(20)
cell2 = Cell(15)

print(cell2.make_order(3))
print(cell1 - cell2)
