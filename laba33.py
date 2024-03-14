import random
popytka = 0
pray = 0

print('добро пожаловать в игру "математика для детей". решите задачу')

while popytka < 3:
    a = random.randint( = 0, = 10)
    b = random.randint( = 0, = 10)
    print(f"{a} + {b} = ', end=")
    if a+b == int(input()):
        print("")
        pray += 1
    else:
        print("")
        popytka += 1
else:
    print("")