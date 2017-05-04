# -- coding: utf-8 --

from datetime import datetime, date, time, timedelta


def my_format_datatime(number):
    """
        Создаёт переменную формата даты из числовой, такой как 19901204 
    """
    str_dt = str(number)
    dt = datetime.strptime(str_dt, "%Y%m%d")
    return dt.date()


def date_number(day, month, year):
    """
         Создаёт переменную формата даты из 3 числовых переменных, содержащих день, месяц и год
    """
    dt = date(year=year, month=month, day=day)
    return dt
