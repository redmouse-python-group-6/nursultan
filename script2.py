# -- coding: utf-8 --
# 2. Выполнить первое задание считав все значения из csv
import csv
from my_pack.translate import translate_csv

translate_csv("price.txt")
reader = csv.reader(open("price.csv"))

keys = set()
count_dict = {}
cur = []
for line_list in reader:
    if len(line_list) == 3:    #  Проверка на правильности списка
        keys.add(line_list[2])
        cur.append(line_list)

for i in keys:
    count_dict[i] = 0

for line in cur:
    for i in keys:
        if line[2] == i:
            count_dict[i] += int(line[1])

out_file = open("price.csv", "a", newline='')
try:
    writer = csv.writer(out_file, delimiter=' ', quoting=csv.QUOTE_MINIMAL, quotechar=' ', lineterminator=' ')
    for k, v in count_dict.items():
        writer.writerow(["\nThe number of", k, "is", v])
finally:
    out_file.close()
