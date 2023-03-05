#Даны два целых числа m и n (m>n). Напишите программу, которая выводит все нечетные числа от m до n включительно в порядке убывания.
m = int(input())
n = int(input())

if m % 2 != 0:
    for i in range(m, n, - 2):
        print(i)
elif m % 2 == 0:
    for i in range(m - 1, n - 1, -2):
        print(i)
elif m - 1 == n:
    for i in range(m, n + 1):
        print(n)