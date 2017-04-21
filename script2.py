# -- coding: utf-8 --

# 5. Переписать первое задание разбив его на модули

from mypack.modul_scr2 import Script2

age = 0
print("Общество в начале XXI века\n")
while True:
    try:
        age = int(input("Введите ваш возраст: "))
        break
    except ValueError:
        print("Пожалуйста введите коректный возраст !!!")


a = Script2(age)