year = int(input("введите год"))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("год " + str(year), "високосный")
else:
    print("обычный")