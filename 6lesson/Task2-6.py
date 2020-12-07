class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        # print(Road.length, Road.width)

    def muss(self):
        weigth = float(input('Введите массу в кг: '))
        height = float(input('Введите высоту в м: '))
        muss_a = self._length * self._width * weigth * height / 1000
        print(f'Масса полотна составляет {muss_a} т.')


r = Road(float(input('Введите длину в м: ')), float(input('Введите ширину в м: ')))
r.muss()
