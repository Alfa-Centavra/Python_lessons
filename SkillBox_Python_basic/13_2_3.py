print('Задача 1. Сумма чисел 2')
#Пользователь вводит число N. Напишите функцию summa_n, которая принимает одно целое положительное число N и находит
#сумму всех чисел от 1 до N включительно. Функция вызывается два раза: сначала от числа N, а затем от полученной суммы.
#Пример работы программы:
#Введите число: 5
#Сумма от 1 до 5 = 15
#Сумма от 1 до 15 = 120

def numb(number):
    summa = 0
    for i in range(2):
        for j in range(1, number + 1):
            summa += j
        
        print(f'Сумма от 1 до {number} = {summa}')
        number = summa
        summa = 0
    
    

number = int(input('Введите число: '))

numb(number)