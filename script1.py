

while True:
    try:
        global x
        x = int(input("Введите число от 1 до 9: "))
        if(x >= 1) and (x <= 9):
            break
        else:
            print("Введите числа только от 1 до 9")
    except(ValueError):
        print("Введите пожалуста только число !!!")


if(x >= 1) and (x <= 3):
    s = input("Введите строку который нужно вывести:  ")
    n = 0
    while True:
        try:
            n = int(input("Введите число повторений:  "))
            break
        except(ValueError):
            print("Введите пожалуста только число !!!")
    for i in range(n):
        print(s)

if(x >= 4) and (x <= 6):
    m = 0
    while True:
        try:
            m = int(input("Введите степень:  "))
            break
        except(ValueError):
            print("Введите пожалуста только число !!!")
    print("%d в степени %d равна %d" % (x, m, x**m))

if(x >= 7) and (x <= 9):
    for i in range(10):
        print(x)
        x += 1