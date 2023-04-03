import math

def myDistance(x, y):
    distance = math.sqrt(x ** 2 + y ** 2)
    print(distance)

def betweenDistance(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    print(distance)

choice = int(input('1 - расстояние до точки; 2 - расстояние между точками: '))
if choice == 1:
    x = float(input('Введите координату х: '))
    y = float(input('Введите координату y: '))
    myDistance(x, y)
elif choice == 2:
    x1 = float(input('Введите координату х первой точки: '))
    y1 = float(input('Введите координату y первой точки: '))

    x2 = float(input('Введите координату х второй точки: '))
    y2 = float(input('Введите координату y второй точки: '))

    betweenDistance(x1, y1, x2, y2)
else:
    print('Ошибка ввода.')