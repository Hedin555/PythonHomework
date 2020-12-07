import time
import itertools


class TrafficLight:
    _color = ()

    def __init__(self):
        TrafficLight._color = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        for x in itertools.cycle(TrafficLight._color):
            print(x)
            if x == 'Красный':
                time.sleep(7)
            elif x == 'Желтый':
                time.sleep(2)
            elif x == 'Зеленый':
                time.sleep(7)


tc = TrafficLight()
tc.running()
