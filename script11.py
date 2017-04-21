# 5. Переписать первое задание разбив его на модули
from mypack.modul_scr1 import Script1

while True:
    try:
        global x
        x = int(input("Введите число от 1 до 9: "))
        if(x >= 1) and (x <= 9):
            break
        else:
            print("Введите числа только от 1 до 9")
    except ValueError:
        print("Введите пожалуста только число !!!")

a = Script1(x)