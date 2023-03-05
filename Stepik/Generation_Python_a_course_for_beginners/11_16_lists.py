#На вход программе подается строка текста, содержащая целые числа. Напишите программу, которая по заданным числам строит столбчатую диаграмму.
numbers = input().split()
sex = ''
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
    sex = int(numbers[i]) * '+'
    print(sex)