# -- coding: utf-8 --
def func(*args):
    """
        функция в которую можно передать сколько угодно значений и оно возводит каждое последующее 
        число в степень предыдущего (первое значение возводит в степень один)
    """
    current = 1
    tmp_list = []
    for i in args:
        tmp_list.append(i ** current)
        current = i
    return tmp_list


def str_int(*args):
    """
        Функция которая берет в аргументы строковый список возращает числовой список 
        если в списке на ходится не числовой символ он отбросит.
    """
    tmp = []
    for elem in args:
        try:
            tmp.append(int(elem))
        except ValueError:
            continue
    return tmp


if __name__ == "__main__":
    print(func.__doc__)
    string = input("Веедите последовательность через пробел:\n")
    elems = string.split()
    c = str_int(*elems)
    print(func(*c))
