#Напишите функцию compute_binom(n, k), которая принимает в качестве аргументов два натуральных числа n и k и возвращает значение биномиального коэффициента, равного f(n)//(f(k)*f(n-k))
from math import factorial as f
# объявление функции
def compute_binom(n, k):
    return f(n)//(f(k)*f(n-k))
    
    



# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))