# -- coding: utf-8 --
# 3. Выполнить первое задание считывая значения из json файла результат выдать в другом json файле

import json
from my_pack.translate import translate_json

translate_json("price.txt")
file = open("price.json")
reader = file.read()
file.close()
reader = json.loads(reader)
keys = set()
count_dict = {}
cur = []
for line_list in reader:
    if len(line_list) == 3:  # Проверка на правильности списка
        keys.add(line_list[2])
        cur.append(line_list)

for i in keys:
    count_dict[i] = 0

for line in cur:
    for i in keys:
        if line[2] == i:
            count_dict[i] += int(line[1])

print(count_dict)
for k, v in count_dict.items():
    reader.append("\nThe number of %s is %d" % (k, v))
json_var = json.dumps(reader)
file = open("price.json", 'w')
file.write(json_var)
file.close()

