
from mypack import modul_scr1

while True:
    try:
        global x
        x = int(input("Введите число от 1 до 9: "))
        if(x >= 1) and (x <= 9):
            break
        else:
            print("Введите числа только от 1 до 9")
    except ValueError:
        print("Введите пожалуста только число !!!")

if(x >= 1) and (x <= 3):
    modul_scr1.option_one()
if(x >= 4) and (x <= 6):
    modul_scr1.option_two(x)
if(x >= 7) and (x <= 9):
    modul_scr1.option_tree(x)