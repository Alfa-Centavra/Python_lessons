print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число, которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.
# Пример: 
# Введите первое число: 102
# Введите второе число: 123
 
# Первое число наоборот: 201
# Второе число наоборот: 321
 
# Сумма: 522
# Сумма наоборот: 225

numb = int(input('Введите первое число: '))
numb_2 = int(input('Введите второе число: '))

reverse_numb = str(numb)[::-1]
reverse_numb_2 = str(numb_2)[::-1]
print('\nПервое число наоборот:', reverse_numb)
print('Второе число наоборот:', reverse_numb_2)

print('\nСумма:', numb + numb_2)
print('Сумма наоборот:', int(reverse_numb) + int(reverse_numb_2))