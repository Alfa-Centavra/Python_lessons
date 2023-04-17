x = input('Выберите операцию: ')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))


while x != '+' and x != '-' and x != '*' and x != '/':
    print('Ошибка: такой операции не существует. Попробуйте ещё раз.')
    x = input('Выберите операцию: ')
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))

else:
    if x == '+':
        print(a + b)
    elif x == '-':
        print(a - b)
    elif x == '*':
        print(a * b)
    elif x == '/':
        print(a / b)
