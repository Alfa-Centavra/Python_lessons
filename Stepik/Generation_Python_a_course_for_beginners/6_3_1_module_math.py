#Напишите программу определяющую евклидово расстояние между двумя точками, координаты которых заданы.
#На вход программе подается четыре вещественных числа, каждое на отдельной строке
#Программа должна вывести одно число – евклидово расстояние.
from math import *
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
p = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
print(p)
