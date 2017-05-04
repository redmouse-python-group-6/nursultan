# -- coding: utf-8 --

from datetime import date, time, datetime, timedelta
import my_modul

# 5. По заданному числу n от 1 до 365 определите, на какое число какого месяца приходится день с номером n.

month_name = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль",
              "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

while True:
    global n
    try:
        n = int(input("Введите количество дней n:\n"))
        break
    except ValueError:
        print("Пожалуйста введите только число !!!")

dt = date.fromordinal(n)

print("Месяц %s приходится день с номером n" % month_name[dt.month-1])


# 6. Решите обратную предыдущей задачу: по дате текущего дня определите номер дня в году.

day = date.today().strftime('%j')

print("%s-й день текущего года" % day)

# 7. Дата задана в формате dd.mm.yyyy. Выведите ее в формате "Month d, y",
#  где Month - английское название месяца, d - номер дня в месяце, без лидирующих
#  нулей, y - номер года без лидирующих нулей

date_str = input("Введит дату через в формате 'дд.мм.гггг':\n")
dt = datetime.strptime(date_str, "%d.%m.%Y")
# dt = dt.date()
str_date = dt.strftime("%B %d %y")
print(str_date)