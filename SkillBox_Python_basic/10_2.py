print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

num = 5
start = 1
for row in range(1, num + 1):
  for col in range(start):
    print(row, end = '\t')
    start = row + 1
  print()