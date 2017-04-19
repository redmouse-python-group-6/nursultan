# -- coding: utf-8 --

# 5. Переписать первое задание разбив его на модули

from mypack import modul_scr2

age = 0

while True:
    try:
        age = int(input("Введите ваш возраст: "))
        break
    except ValueError:
        print("Пожалуйста введите коректный возраст !!!")

print(age)
print(modul_scr2.func(age))
