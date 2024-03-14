a = int(input("ваш номер:"))
if a in range(0,35) and a % 2 == 0:
    print("нижнее место")
elif a in range(0,35) and a % 2 != 0:
    print("верхнее место")

if a in range(35,54) and a % 2 == 0:
    print("нижнее боковое место")
elif a in range(35,54) and a % 2 != 0:
    print("верхнее боковое место")