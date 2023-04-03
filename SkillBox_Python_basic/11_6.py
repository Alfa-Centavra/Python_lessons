print('Задача 6. Ход конём')
# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
# 
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

print('Введите местоположение коня: ')
x = float(input())
y = float(input())

xSquare = int(x * 10)
ySquare = int(y * 10)

print('Введите местоположение точки на доске: ')
xNext = float(input())
yNext = float(input())

xNextSquare = int(xNext * 10)
yNextSquare = int(yNext * 10)

print(f'Конь в клетке {xSquare, ySquare}. Точка в клетке {xNextSquare, yNextSquare}.')
if 0 <= x <= 8 and 0 <= y <= 8:
    if xNextSquare == xSquare + 2 and yNextSquare == ySquare + 1 or xNextSquare == xSquare - 2 and yNextSquare == ySquare - 1 or xNextSquare == xSquare - 2 and yNextSquare == ySquare + 1 or xNextSquare == xSquare + 2 and yNextSquare - 1:
        print('Да, конь может ходить в эту точку')
    elif xNextSquare == xSquare + 1 and yNextSquare == ySquare + 2 or xNextSquare == xSquare - 1 and yNextSquare == ySquare - 2 or xNextSquare == xSquare - 1 and yNextSquare == ySquare + 2 or xNextSquare == xSquare + 1 and yNextSquare - 2:
        print('Да, конь может ходить в эту точку')
    else:
        print('Данный ход не возможен')
