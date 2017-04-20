# -- coding: utf-8 --

# 3. Написать программу которая заполняет случайным текстом строку.
#       a. Попросить ввести  символы пользователя
#       b. Заменить регулярным выражением Это слово на ее
#          ревертированное значение если это слово в начале
#          или конце это предложения


import random
import re

alphabet_chars = "abcdefghijklmnopqrstuvwxyz"
random_lst = []

for i in range(random.randint(2, 10)):
    word = []
    for j in range(random.randint(3, 8)):
        word.append(random.choice(alphabet_chars))
    word = ''.join(word)
    random_lst.append(word)

random_str = ' '.join(random_lst)
print("случайный текст:\n", random_str)
word = input("Введите слово: ")
revers_word = word[:: -1]
print("Реверсивный вид ", revers_word)
new_str = re.sub(r"%s|%s$" % (word, word), revers_word, random_str)
print(new_str)