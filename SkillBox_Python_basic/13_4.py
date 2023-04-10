def count_numbers(number):
    count = 0
    while number != 0:
        count += 1
        number //= 10
    return count


def change_number(number):
    last_digit = number % 10
    first_digit = number // 10**(count_numbers(number) - 1)
    between_digits = number % 10**(count_numbers(number) - 1) // 10
    number = last_digit * 10**(count_numbers(number) - 1) + between_digits * 10 + first_digit
    return number


number_1 = int(input('Введите первое число: '))
count_numbers(number_1)
if count_numbers(number_1) < 3:
    print("В первом числе меньше трёх цифр.")
else:
    print(f"Первое число наоборот: {change_number(number_1)}")

number_2 = int(input('\nВведите второе число: '))
count_numbers(number_2)
if count_numbers(number_2) < 4:
    print("Во втором числе меньше четырёх цифр.")
else:
    print(f"Второе число наоборот: {change_number(number_2)}")
    print(f"\nСумма измененных чисел: {change_number(number_1) + change_number(number_2)}")

