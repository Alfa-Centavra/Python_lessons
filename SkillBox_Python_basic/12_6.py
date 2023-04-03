print('Задача 6. НОД')

#Напишите функцию, вычисляющую наибольший общий делитель двух чисел


def nod():
    first = int(input('Введите первое число: '))
    second = int(input('Введите второе число: '))
    a = first
    b = second 
    while first != second:
        if first > second:
            first = first - second
        else:
            second = second - first
    print(f'НОД чисел {a} и {b} равен {first}')

nod()