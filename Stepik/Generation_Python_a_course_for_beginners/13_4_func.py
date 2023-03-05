#Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую количество делителей данного числа.
#Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.
# объявление функции
def number_of_factors(num):
    l = []
    for i in range(1, n + 1):
        if n % i == 0:
            l.append(i)
    return len(l)

# считываем данные
n = int(input())

# вызываем функцию
print(number_of_factors(n))