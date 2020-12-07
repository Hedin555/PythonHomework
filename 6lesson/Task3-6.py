class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_full_profit(self):
        return sum(self._income.values())


worker1 = Position(input('Введите имя: '),
                   input('Введите фамилию: '),
                   input('Введите должность: '),
                   int(input('Введите оклад: ')),
                   int(input('Введите бонус: ')))
print(f'ФИО: {worker1.get_full_name()}\nЗарплата: {worker1.get_full_profit()}')
