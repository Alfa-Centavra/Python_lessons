while True:
    command = input("Выберите операцию: ")
    if command in "+-*/":
        break
    print("Ошибка: такой операции не существует. Попробуйте ещё раз.")


count = int(input('Сколько операндов? '))
for count_number in range(1, count + 1):
    number = int(input(f'Введите операнд {count_number}: '))
    if count_number == 1:
        number_result = number
        continue
    if command == '+':
        number_result += number
    elif command == '-':
        number_result -= number
    elif command == '*':
        number_result *= number
    elif command == '/':
        number_result /= number
    print(number_result)
    print('****')
print(number_result)
