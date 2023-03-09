n = int(input('Сколько чисел: '))
k = int(input('Какую цифру ищем: '))
count = 0
while 0 > k > 9:
  k = int(input('Цифра должна быть в диапозоне от 0 до 9: '))
for num in range(n):
  print('Введите', num, 'число: ', end = '')
  number = int(input())
  while number > 0:
    if number % 10 == k:
      count += 1
    number //= 10
print('Цифр', k, 'в последовательности:', count)