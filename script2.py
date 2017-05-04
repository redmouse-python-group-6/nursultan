# -- coding: utf-8 --

from datetime import date, time, datetime, timedelta
import my_modul

#  3. Переводим строчную переменную в формат даты

str_date_time = "15/12/1995 12:15:00"
str_date_time2 = "15.05.17 13:00"

dt = datetime.strptime(str_date_time, "%d/%m/%Y %H:%M:%S")
dt2 = datetime.strptime(str_date_time2, "%d.%m.%y %H:%S")

print(dt)
print(dt2)


#  4. Отнять от даты на текущей даты месяц сохранить в переменную и
#  потом к этой переменной добавить один год и определить какой это по счету день

dt_now = date.today()

dt = date(day=dt_now.day, month=dt_now.month-1, year=dt_now.year)
day = dt - date(day=1, month=1, year=dt_now.year)

print("Ответ: ", day)