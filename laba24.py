color1 = input("Введите 1 цвет: ")
color2 = input("Введите 2 цвет: ")

if color1 != "красный" and color1 != "синий" and color1 != "желтый":
    print("Используйте другой 1 цвет: красный, синий или желтый")
elif color2 != "красный" and color2 != "синий" and color2 != "желтый":
    print("Используйте другой 2 цвет: красный, синий или желтый")
elif color1 == "красный" and color2 == "синий" or color2 == "красный" and color1 == "синий":
    print("Получится фиолетовый")
elif color1 == "красный" and color2 == "желтый" or color2 == "красный" and color1 == "желтый":
    print("Получится оранжевый")
elif color1 == "синий" and color2 == "желтый" or color2 == "синий" and color1 == "желтый":
    print("Получится зеленый")
else:
    print('Получится', color1)