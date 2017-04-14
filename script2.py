print("Общество в начале XXI века\n\n")

age = 0

while True:
    try:
        age = int(input("Введите ваш возраст: "))
        break
    except(ValueError):
        print("Пожалуйста введите коректный возраст !!!")

if(age >= 0) and (age < 7):
    print("Вам в детский сад")

elif(age >= 7) and (age < 18):
    print("Вам школу")

elif(age >= 18) and (age < 25):
    print("Вам в профессиональное учебное заведение")

elif(age >= 25) and (age < 60):
    print("Вам на работу")

elif(age >= 60) and (age <= 120):
    print("Вам предоставляется выбор")
else:
    a = "Ошибка! Это программа для людей!\n"
    print(a*5)