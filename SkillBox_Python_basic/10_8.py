print('Задача 8. Яма ')

# Представьте, что вы разрабатываете компьютерную игру с текстовой графикой. Вам поручили создать генератор ландшафта. Напишите программу, которая получает на вход число N и выводит на экран числа в виде ямы:

# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345
num = int(input('Введите число: '))
colled = num
list = []
list_revers = []
for row in range(1, num + 1):
    for col in range(1, num + 1):
        list.append(num)
        list_revers.insert(0, num)
        if row < num:
            print(*list, '.' * ((colled - col) * 2), *list_revers, sep = '', end = '')
            num -= 1
        elif row == num:
            print(*list, *list_revers, sep = '', end = '')
        print()

#depth = int(input('Введите число: '))
#for line in range(depth):
#    for left_number in range(depth, depth - line - 1, - 1):
#        print(left_number, end = '')
#    point_count = 2 * (depth - line - 1)
#    print('.' * point_count, end = '')
#    for right_number in range(depth - line, depth + 1):
#        print(right_number, end = '')
#    print()