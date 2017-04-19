# -- coding: utf-8 --
from mypack.funcrange import func, str_int  # импортируем из пакета mypack модули funcrange и word_len
from mypack.word_len import word_len_print


# 3. Напишите функцию, которая разбивает введённую строку на слова и выводит по очереди само слова тире ее длина.

string = input("Введите строку: ")
word_len_print(string)

# 4. аписать функцию в которую можно передать сколько угодно значений и оно возводит каждое последующее число в
# степень предыдущего (первое значение возводим в степень один)

string = input("Веедите последовательность через пробел:\n")
elems = string.split()
num = str_int(*elems)  # переводим строковые символы в числовые print(funcrange.str_int.__doc__)
print(func(*num))  # print(funcrange.func.__doc__)
