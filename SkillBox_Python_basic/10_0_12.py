#Пользователь вводит последовательность из N чисел. Напишите программу, которая подсчитывает общее количество цифр больше пяти во всей последовательности.

n = int(input('Сколько чисел: '))
count = 0
for num in range(n):
  print('Введите', num, 'число: ', end = '')
  number = int(input())
  while number > 0:
    if number % 10 > 5:
      count += 1
    number //= 10
print('Цифр больше 5 в последовательности:', count)