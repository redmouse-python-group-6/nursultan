#   2.  Написать абстрактный класс в котором будет только один
#   атрибут который и есть введённое нами число  по умолчанию
#   в конструкторе задается значение ноль

from abc import ABCMeta, abstractmethod, abstractproperty


class Cyrcle():
    __metaclass__ = ABCMeta

    @abstractproperty
    def radiuse(self):
        """Радиус круга"""


class PainCyrcle(Cyrcle):
    radiuse = 0

    def __init__(self, x, y,radiuse=0):
        self.x = x
        self.y = y
        self.radiuse = radiuse

    def show(self):
        print("X = %d, Y = %d, Radiuse = %d." % (self.x, self.y, self.radiuse))

a = PainCyrcle(12, 15, 15)
a.show()