#Даны три вещественных числа a, b, c. Напишите программу, которая находит вещественные корни квадратного уравнения 
#На вход программе подается три вещественных числа a ≠ 0,b,c, каждое на отдельной строке.

from math import *
a = float(input())
b = float(input())
c = float(input())
d = b ** 2 - 4 * a * c
x = 0
if d < 0:
    print('Нет корней')
elif d == 0:
    x = - (b / (2 * a))
    print(x)
elif d > 0:
    x1 = (-b + sqrt(d)) / (2 * a)
    x2 = (-b - sqrt(d)) / (2 * a)
    print(min(x1, x2))
    print(max(x1, x2))