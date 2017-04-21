# -- coding: utf-8 --

class Script2:
    val = 0

    def __init__(self, age):
        self.val = age
        self.func1()
        self.func2()
        self.func3()
        self.func4()
        self.func5()
        self.func6()

    def func1(self):
        if (self.val >= 0) and (self.val < 7):
            print("Вам в детский сад")

    def func2(self):
        if (self.val >= 7) and (self.val < 18):
            print("Вам школу")

    def func3(self):
        if (self.val >= 18) and (self.val < 25):
            print("Вам в профессиональное учебное заведение")

    def func4(self):
        if (self.val >= 25) and (self.val < 60):
            print("Вам на работу")

    def func5(self):
        if (self.val >= 60) and (self.val <= 120):
            print("Вам предоставляется выбор")

    def func6(self):
        if (self.val < 0) or (self.val > 120):
            a = "Ошибка! Это программа для людей!\n"
            print(a * 5)

if __name__ == "__main__":
    age = 0
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            break
        except ValueError:
            print("Пожалуйста введите коректный возраст !!!")
    a = Script2(age)
