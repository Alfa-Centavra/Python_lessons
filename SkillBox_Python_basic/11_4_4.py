print('Задача 2.Игра')
import math

distance = float(input('Введите пройденное расстояние: '))
angle = float(input('Введите угол в градусах: '))

angle /= 57.2958

x = distance * math.cos(angle)
y = distance * math.sin(angle)

print(f'координаты нового местоположения персонажа: ({x}, {y})')