class Stationery:
    atr_title = 'Title'

    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationery):
    def draw(self):
        print('Для записей')


class Pencil(Stationery):
    def draw(self):
        print('Для рисунков')


class Handle(Stationery):
    def draw(self):
        print('Для выделения текста')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
