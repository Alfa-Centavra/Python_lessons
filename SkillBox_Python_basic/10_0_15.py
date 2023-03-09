#bankomat - for
for attemt in range(3):
  print('Осталось попыток: ', 3 - attemt)
  password = int(input('Введите пароль: '))
  if password != 0000:
    attemt += 1
    print('Пароль неверный, попробуйте ещё раз')
    if attemt == 3:
      print('Ваша карта заблокирована!')
  else:
    print('Пароль верный! ')
    break
  print()
