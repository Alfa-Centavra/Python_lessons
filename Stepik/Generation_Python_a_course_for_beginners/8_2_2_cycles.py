#На вход программе подается одно натуральное число, состоящее как минимум из трех цифр.
#Программа должна вывести его третью (с начала) цифру.

n = int(input())
while n > 99:
    if n <= 999:
        n = n % 10
    elif n > 999:
        x = n % 10
        n = n // 10
print(n)