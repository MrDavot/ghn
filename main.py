x1 = int(input("Введите номер (от 1 до 8): "))
y1 = int(input("Введите номер (от 1 до 8): "))
x2 = int(input("Введите номер (от 1 до 8): "))
y2 = int(input("Введите номер (от 1 до 8): "))
if (x1 + y1) % 2 == (x2 + y2) % 2:
    result = "YES"
else:
    result = "NO"

print("Клетки покрашены в один цвет:", result)