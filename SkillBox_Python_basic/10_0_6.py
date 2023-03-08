size = int(input('Введите размер таблицы: '))
for row in range(1, size + 1):
  for col in range(1, size + 1):
    if col == 3:
      print(3, end = ' ')
    else:
      print(row, end = ' ')
    if col == 6:
      print(size, end = ' ')
  print()
