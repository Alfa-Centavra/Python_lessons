#Напишите программу, в которой рассчитывается сумма и произведение цифр положительного трёхзначного числа.
#На вход программе подаётся положительное трёхзначное число.
#Программа должна вывести два числа с поясняющим текстом: сумма цифр и произведение цифр.

a = int(input())
a1 = a % 10
a2 = (a // 10) % 10
a3 = a // 100
print('Сумма цифр =', a1 + a2 + a3)
print('Произведение цифр =', a1 * a2 * a3)