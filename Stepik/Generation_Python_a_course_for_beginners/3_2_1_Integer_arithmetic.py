#Напишите программу, которая считывает два целых числа a и b и выводит на экран квадрат суммы и сумму квадратов

a = int(input())
b = int(input())
a1 = (a + b) ** 2
a2 = a ** 2 + b ** 2
print('Квадрат суммы', a, 'и', b, 'равен', a1)
print('Сумма квадратов', a, 'и', b, 'равна', a2)