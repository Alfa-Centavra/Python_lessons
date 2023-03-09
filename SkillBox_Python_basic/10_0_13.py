#Пользователь вводит число N. Напишите программу, которая по этому числу выводит вот такую лестницу из чисел:

n = int(input('Сколько чисел: '))
start = 0
for i in range(start, n + 1):
  for k in range(start, n + 1):
    print(k, end = ' ')
  start += 1  
  print()