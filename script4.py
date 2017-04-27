# -- coding: utf-8 --

# 4. Сохранить в json структуру любой папки у Вас на компьютере

import os
import json


def walk(dir):
    content = list()
    dirrect = {}
    for name in os.listdir(dir):
        path = os.path.join(dir, name)
        if os.path.isfile(path):
            content.append(name)
        else:
            dirrect[name] = walk(path)
            content.append(dirrect)
    return content

json_var = json.dumps(walk('./my_pack'))
file = open("struct_dir.json", 'w')
file.write(json_var)
file.close()
