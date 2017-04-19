# -- coding: utf-8 --
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


def option_two(x):
    m = 0
    while True:
        try:
            m = int(input("Введите степень:  "))
            break
        except ValueError:
            print("Введите пожалуста только число !!!")
    print("%d в степени %d равна %d" % (x, m, x ** m))


def option_tree(x):
    lst = [x + i for i in range(10)] # генерируем список
    for i in lst:
        print(i)


if __name__ == "__main__":
    print("Module name modul_scr1 ")