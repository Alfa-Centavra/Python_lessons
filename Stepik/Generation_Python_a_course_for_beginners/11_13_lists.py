#На вход программе подается натуральное число n, затем n строк, затем число k — количество поисковых запросов, затем k строк — поисковые запросы. Напишите программу, которая выводит все введенные строки, в которых встречаются все поисковые запросы.
#На вход программе подаются натуральное число n — количество строк, затем сами строки в указанном количестве, затем число k, затем сами поисковые запросы.

# put your python code here
n = int(input())
a = []
b = []
for i in range(n):
    s = input()
    a.append(s)
k = int(input())
for j in range(k):
    e = input()
    b.append(e)
for i in range(len(a)):
    count= 0
    for j in range(len(b)):
        if b[j].lower() in a[i].lower():
            count += 1
    if count == len(b):
        print(*a[i], sep = '')
