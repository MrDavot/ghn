x = float(input("Введите число: "))

if x > 0:
    result = 1
elif x < 0:
    result = -1
else:
    result = 0

print("Знак числа:", result)