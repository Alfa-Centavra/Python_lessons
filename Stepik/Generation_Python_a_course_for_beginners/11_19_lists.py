#На вход программе подается строка текста, содержащая различные натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая меняет местами минимальный и максимальный элемент этого списка.
l = input().split()
for i in range(len(l)):
    l[i] = int(l[i])
a = l.index(max(l))
b = l.index(min(l))
l[a], l[b] = l[b], l[a]
print(*l)