print('Задача 4. Простые числа')

# Напишите программу, которая считает количество простых чисел в заданной последовательности и выводит ответ на экран.

# Простое число делится только на себя и на единицу. Последовательность задаётся при помощи вызова ввода (input) на каждой итерации цикла. Одна итерация — одно число.

# Пример:
# Введите количество чисел: 6.
# Введите число: 4.
# Введите число: 7.
# Введите число: 20.
# Введите число: 3.
# Введите число: 11.
# Введите число: 37.

# Количество простых чисел в последовательности: 4.
numCount = int(input('Введите количество чисел: '))
count = 0
allCount = 0
for i in range(numCount):
  number = int(input('Введите число: '))
  for j in range(2, number - 1):
    if number % j == 0:
      count += 1
      if count != 0:
        allCount += 1
        count = 0
        break

print('Количество простых чисел в последовательности:', numCount - allCount)
  