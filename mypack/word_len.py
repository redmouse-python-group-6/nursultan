# -- coding: utf-8 --
class WordLen:
    string = ""

    def __init__(self, string):
        self.string = string
        self.word_len_print()

    def word_len_print(self,  delimiter=" "):
        """ 
            функция которая разбивает введённую строку на слова
            и выводит по очереди само слова тире ее длина.
        """
        words = self.string.split(delimiter)
        for word in words:
            print("%s - %d" % (word, len(word)))


if __name__ == "__main__":
    string = input("Введите строку: ")
    a = WordLen(string)


