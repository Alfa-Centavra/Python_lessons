print('Задача 3. Апгрейд калькулятора')
# Степан использует калькулятор для расчёта суммы и разности чисел, но на работе ему требуются не только обычные арифметические действия. 
# Он ничего не хочет делать вручную, поэтому решил немного расширить функционал калькулятора.
# Напишите программу, запрашивающую у пользователя число и действие, которое нужно сделать с числом: вывести сумму его цифр,
# максимальную или минимальную цифру. 
#Каждое действие оформите в виде отдельной функции, а основную программу зациклите.
# Запрошенные числа должны передаваться в функции суммы, максимума и минимума при помощи аргументов.
import math

l = []

def summ():
    l.append(num)
    print(f'Сумма чисел равна: {sum(l)}')

def maxx():
    l.append(num)
    print(f'Максимальное число равно: {max(l)}')

def minn():
    l.append(num)
    print(f'Минимальное число равно: {min(l)}')


while True:
    num = int(input('Введите число: '))
    active = int(input('Какое действие хотите выполнить с числом: 1 - вывести сумму его цифр; 2 - вывести максимальную цифру; 3 - вывести минимальную цифру; 0 - завершить работу. '))
    if active == 1:
        summ()
    elif active == 2:
        maxx()
    elif active == 3:
        minn()
    elif active == 0:
        print('До встречи!')
        break
    else:
        print('Ошибка ввода! Попробуйте ещё раз')

