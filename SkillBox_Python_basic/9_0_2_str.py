count_2 = 0
for student in range(5):
  quest = input('Кто написал "Война и мир?" ').title()
  print(quest)
  if quest == 'Толстой':
    print('Молодец!')
    break
  print('Неправильно! Два!')
  count_2 += 1
  
print('Кол-во двоечников:', count_2)