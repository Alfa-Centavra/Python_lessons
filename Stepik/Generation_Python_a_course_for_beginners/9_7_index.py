#На вход программе подается одна строка. Напишите программу, которая определяет сколько в ней одинаковых соседних символов.
# put your python code here
n = input()
count = 0
for i in range(len(n) - 1):
    if n[i] == n[i + 1]:
        count += 1
print(count)