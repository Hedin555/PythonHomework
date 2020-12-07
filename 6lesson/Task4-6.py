class Cars:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.max_speed = 300

    def go(self):
        return "Машина двигается"

    def stop(self):
        return "Машина остановилась"

    def turn_left(self):
        return "Машина повернула налево"

    def turn_right(self):
        return "Машина повернула направо"

    def show_speed(self):
        if self.speed > self.max_speed:
            return 'Скорость машины превышена'
        else:
            return self.speed
        # Не пойму, почему если ставлю print(f'Текущая скорость{self.speed}')
        # выводит кроме значения скорости второй строчкой None


class TownCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.max_speed = 60


class SportCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)


class WorkCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.max_speed = 40


class PoliceCar(Cars):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.is_police = True


nissan = WorkCar(70, 'Зеленый', 'Ниссан')
hundai = PoliceCar(120, 'Черный', 'Хундай')
ford = TownCar(90, 'Белый', 'Форд')
mazda = SportCar(270, 'Красный', "Мазда")
print(f'марка {ford.name}, цвет {ford.color}, движется со скоростью {ford.speed}')
print(ford.show_speed())
print(f'{ford.turn_right()} {ford.stop()}')
