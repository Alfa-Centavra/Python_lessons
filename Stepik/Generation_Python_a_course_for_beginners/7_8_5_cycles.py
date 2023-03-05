#Дано натуральное число n. Напишите программу, которая выводит значение суммы
n = int(input())
fac = 1
counter = 0

for i in range(1, n +1):
    fac *= i
    counter += fac
print(counter)