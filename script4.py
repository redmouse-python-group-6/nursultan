#  4. Создаем конечный класс в котором наследуем два предыдущих класса в нем же перегружаем конструктор

from mypack.modul_scr2 import Script2
from mypack.modul_scr1 import Script1


class Script4(Script1, Script2):
    def __init__(self, x):
        if (x >= 1) and (x <= 9):
            print("Выпоняется скрипт № 1: ")
            Script1.__init__(self, x)
            print("\n")
        Script2.__init__(self, x)

while True:
    try:
        global x
        x = int(input("Введите число:\n"))
        break
    except ValueError:
        print("Пожалуста введите только число !!!")
a = Script4(x)
