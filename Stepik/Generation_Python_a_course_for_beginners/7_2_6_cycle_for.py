#На вход программе подается натуральное число n. Напишите программу, которая вычисляет n!.
from math import *
n = int(input())
for i in range(1, n + 1):
    n = factorial(i)
print(n)