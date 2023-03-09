#Bankomat - while
while True:
  print('Добро пожаловать! ')
  for attemt in range(3):
    print('Осталось попыток: ', 3 - attemt)
    password = int(input('Введите пароль: '))
    if password != 0000:
      attemt += 1
      if attemt == 3:
        print('Ваша карта заблокирована!')
      else:
        print('Пароль неверный, попробуйте ещё раз')
    else:
      print('Пароль верный! ')
      break
    print()
  print('\nСледующий клиент! ', end = ' ')



