#Назовем число красивым, если оно является четырехзначным и делится нацело на 7 или на 17. Напишите программу, определяющую, является ли введённое число красивым. Программа должна вывести «YES», если число является красивым, или «NO» в противном случае.
i = int(input())

if i >= 1000 and i <= 9999 and (i % 17 == 0 or i % 7 == 0):
    print('YES')
else:
    print('NO')