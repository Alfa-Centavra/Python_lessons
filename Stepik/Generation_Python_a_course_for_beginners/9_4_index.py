#На вход программе подается одна строка состоящая из цифр. Напишите программу, которая считает сумму цифр данной строки.
# put your python code here
n = input()
count = 0
for c in n:
    count += int(c)
print(count)