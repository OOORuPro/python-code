from random import randint

switch=True

while True==switch:
    a = int(input('От: \n'))
    b = int(input('До: \n'))

    res = randint(a,b)

    print("Сгенерированное число: ",int(res),"\n")
