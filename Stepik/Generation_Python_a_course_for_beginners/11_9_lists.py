#На вход программе подается натуральное число n≥2, а затем n целых чисел. Напишите программу, которая создает из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и т.д.).
#На вход программе подаются натуральное число n, а затем n целых чисел, каждое на отдельной строке.
# put your python code here
n = int(input())
l = list()
count = 0
for i in range(n):
    c = int(input())
    count += c
    l.append(count)
    count = c
print(l[1:])

