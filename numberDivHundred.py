connect = True
number = 0
procent = 0
while connect == True:

    while type(number) != int:
        try:
            number = int(input("Число: "))
            procent = int(input("Процент: "))
        except ValueError:
            print("Вводите целочисленные значения!")
            number = input("Введите число: ")
            procent = input("Введите процент: ")
    while type(number) != float:
        try:
            number = float(input("Число: "))
            procent = float(input("Процент: "))
        except ValueError:
            print("Вводите целочисленные значения!")
            number = input("Введите число: ")
            procent = input("Введите процент: ")

    finish = number * procent / 100
    print("Результат: ", int(finish))
