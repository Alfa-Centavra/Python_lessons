#Числовая угадайка

import random

test_number = random.randint(1, 100)

while test_number:
    guess_number = int(input('Угадай число от 1 до 100: '))

    if guess_number > test_number:
        print('Слишком много, попробуйте еще раз')
        continue
    if guess_number < test_number:
        print('Слишком мало, попробуйте еще раз')
        continue
    else:
        print('Вы угадали, поздравляем!')
        break