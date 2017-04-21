# -- coding: utf-8 --
class Script1:
    x = 0

    def __init__(self, x):
        self.x = x
        if (self.x >= 1) and (self.x <= 3):
            self.option_one()
        if (self.x >= 4) and (self.x <= 6):
            self.option_two()
        if (self.x >= 7) and (self.x <= 9):
            self.option_tree()

    @staticmethod
    def option_one():
        s = input("Введите строку который нужно вывести:  ")
        n = 0
        while True:
            try:
                n = int(input("Введите число повторений:  "))
                break
            except ValueError:
                print("Введите пожалуста только число !!!")
        lst = [s for i in range(n)]  # генерируем список
        for el in lst:
            print(el)

    def option_two(self):
        m = 0
        while True:
            try:
                m = int(input("Введите степень:  "))
                break
            except ValueError:
                print("Введите пожалуста только число !!!")
        print("%d в степени %d равна %d" % (self.x, m, self.x ** m))

    def option_tree(self):
        lst = [self.x + i for i in range(10)]  # генерируем список
        for i in lst:
            print(i)


if __name__ == "__main__":
    print("class Script1")