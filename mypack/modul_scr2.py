# -- coding: utf-8 --
def func(val):
    """
        Функция испльзуется первой задании в втором скрипте. Функция принимает в качестве аргумента 
        возраст возвращает строку.
    """
    if (val >= 0) and (val < 7):
        return "Вам в детский сад"

    elif (val >= 7) and (val < 18):
        return "Вам школу"

    elif (val >= 18) and (val < 25):
        return "Вам в профессиональное учебное заведение"

    elif (val >= 25) and (val < 60):
        return "Вам на работу"

    elif (val >= 60) and (val <= 120):
        return "Вам предоставляется выбор"
    else:
        a = "Ошибка! Это программа для людей!\n"
        return a * 5

if __name__ == "__main__":
    print(func.__doc__)
