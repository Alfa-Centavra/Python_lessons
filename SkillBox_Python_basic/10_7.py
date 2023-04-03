print('Задача 7. Пирамидка 2')
# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
# 
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29
height = int(input("Введите количество уровней: "))
num = 1
for row in range(1, height + 1):
  print('\t' * (height - row), end = '')
  for col in range(row):
    print(num, end = '')
    num += 2
    print('\t' * 2, end = '')
  print()