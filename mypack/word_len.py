# -- coding: utf-8 --

def word_len_print(string, delimiter=" "):
    """ 
        функция которая разбивает введённую строку на слова
        и выводит по очереди само слова тире ее длина.
    """
    words = string.split(delimiter)
    for word in words:
        print("%s - %d" % (word, len(word)))


if __name__ == "__main__":
    print(word_len_print.__doc__)
    string = input("Введите строку: ")
    word_len_print(string)


