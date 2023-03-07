string = input('Введите строку: ') #aabc
prevSym = ''
equalSym = False
for symbol in string:
  if prevSym == symbol:
    equalSym = True
  else:
    prevSym = symbol

if equalSym:
  print('Есть две одинаковые буквы подряд!')
else:
  print('Нету одинаковых букв подряд!')