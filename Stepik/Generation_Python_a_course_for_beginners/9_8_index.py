#На вход программе подается натуральное число, записанное в десятичной системе счисления. Напишите программу, которая переводит данное число в двоичную систему счисления.
# put your python code here
n = int(input())
s =''
while n > 0:
    a = n % 2
    s = str(a) + s
    n //= 2
print(s)