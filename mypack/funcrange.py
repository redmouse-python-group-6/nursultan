# -- coding: utf-8 --


class FuncRancge:
    args = []

    def __init__(self, string):
        elems = string.split()
        self.args = self.str_int(*elems)
        self.print_result()

    def input_args(self):
        string = input("Веедите последовательность через пробел:\n")
        elems = string.split()
        self.args = self.str_int(*elems)

    def print_result(self):
        print(self.func(*self.args))

    @staticmethod
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

    @staticmethod
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
    string = input("Веедите последовательность через пробел:\n")
    a = FuncRancge(string)

