# -- coding: utf-8 --

# 1. Дан файл с прайс листом одежды. Помимо названия товара указывается количество штук и количество пар.
# В одной строке указывается только один товар. Посчитать количество товаров которые считаются штуками
# и количество товаров считаемых парами.  Результаты дописать в конец файла

file = open("price.txt", 'r')
lines = file.readlines()
file.close()
keys = set()
count_dict = {}
cur = []
for line in lines:
    line_list = line.split()
    if len(line_list) == 3:    #  Проверка на правильности списка
        keys.add(line_list[2])
        cur.append(line_list)
print(keys)
for i in keys:
    count_dict[i] = 0

for line in cur:
    for i in keys:
        if line[2] == i:
            count_dict[i] += int(line[1])


print(count_dict)

file = open("price.txt", 'a')
for k, v in count_dict.items():
    file.write("\n\nThe number of %s is %d" % (k, v))
file.close()


