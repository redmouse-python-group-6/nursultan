# -- coding: utf-8 --

from datetime import date, time, datetime, timedelta
import my_modul

#  1. Создаём переменную формата даты из числовой, такой как 19901204

while True:
    global num_data
    try:
        num_data = int(input("Введите дату в числовом формате такой как '19900212':\n"))
        break
    except ValueError:
        print("Пожалуйста введите только число !!!")

dt = my_modul.my_format_datatime(num_data)

print(dt)
print(type(dt))


#  2. Создаём переменную формата даты из 3 числовых переменных, содержащих день, месяц и год
while True:
    global day
    try:
        day = int(input("Введите день:\n"))
        break
    except ValueError:
        print("Пожалуйста введите только число !!!")

while True:
    global month
    try:
        month = int(input("Введите месяц:\n"))
        break
    except ValueError:
        print("Пожалуйста введите только число !!!")

while True:
    global year
    try:
        year = int(input("Введите год:\n"))
        break
    except ValueError:
        print("Пожалуйста введите только число !!!")

dt = my_modul.date_number(day, month, year)

print(dt)




