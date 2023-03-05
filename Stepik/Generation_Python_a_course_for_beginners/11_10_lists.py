#На вход программе подается натуральное число n и n строк, а затем число k. Напишите программу, которая выводит k-ую букву из введенных строк на одной строке без пробелов.
# put your python code here
n = int(input())
l = []
for i in range(n):
    a = input()
    l.append(a)
k = int(input())
x1 =''
x2 =''
for j in range(n):
    if k <= len(l[j]):
        x1 = l[j][k - 1]
        x2 += x1
print(x2, end = '')