#Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.
n = int(input())
x = n % 10
count = 0

while n != 0:
    y = n % 10
    n = n // 10
    if x != y:
        count += 1
if count != 0:
    print('NO')
else:
    print('YES')