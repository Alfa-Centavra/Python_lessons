count = int(input('Введите количество человек: '))
for hour in range(count + 1):
  print('Идёт час:', hour)
  for num in range(hour, count):
    print('Номер в очереди: ', num)
  print()
print('Очередь обслужена!')