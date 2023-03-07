#Используя новые знания с циклами и оператором end, выведете на экран “доску”, которую вы делали в первом модуле
print('-' * 10)
for _ in range(4):
  for j in range(10):
    if j == 0 or j == 9:
      print('|', end = '')
    else:
      print('0', end = '')
  print()
print('-' * 10)