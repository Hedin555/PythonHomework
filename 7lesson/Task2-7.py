from abc import ABC, abstractmethod
class Clothers(ABC):

    def __init__(self, fabric):
        self.fabric = fabric

    @abstractmethod
    def calculation(self):
        pass

class Suit(Clothers):

    def calculation(self):
        return round(2 * self.fabric + 0.3)


class Coat(Clothers):

     def calculation(self):
        return round(self.fabric/6.5 + 0.5)

coat = Coat(float(input('Введите размер для пальто: ')))
print(f'Ткани на пальто требуется: {coat.calculation()}')
suit = Suit(float(input('Введите рост для костюма: ')))
print(suit.calculation())