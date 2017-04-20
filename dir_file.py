# -- coding: utf-8 --

# Написать программу которая в интерактивном режиме просит ввести путь к папкам.
# Затем просит ввести название папки/файла. Затем если по заданному пути находится файл/папка
# то выводить: ее полный путь, размер, тип объекта (файл или директория), дату создания изменения объекта.

import os
from datetime import datetime

while True:
    global abs_path
    pwd = input("Введите путь к папке:\n")
    name = input("Введите имя файла/папки:\n")
    path = os.path.join(pwd, name)
    abs_path = os.path.abspath(path=path)
    if os.path.exists(abs_path):
        break
    else:
        print("Непрвильно задан путь или токого файла.директории не сушествует !!!")
size = os.path.getsize(abs_path)
creat_date = os.path.getctime(abs_path)
change_date = os.path.getmtime(abs_path)
type_fd = "Фаил"
fd_list = []

if os.path.isdir(abs_path):
    type_fd = "Директория"
    fd_list = os.listdir(abs_path)

print("Полный путь: ", abs_path)
print("Размер: %s байт" % size)
print("Тип:", type_fd)
print("Дата создания: ", datetime.fromtimestamp(creat_date))  # поскольку os.path.getctime() возвращает количство секунд
print("Дата последнего изменения: ", datetime.fromtimestamp(change_date))
if type_fd == "Директория":
    print("Содержания директории: ")
    for fd in fd_list:
        print("     ", fd)
