def triangle():
  stars = 1
  for line in range(5):
    print(' ' * (5 - line - 1), end = '')
    print('*' * stars)
    stars += 2
    
def rectangle():
  for line in range(5):
    if line == 0 or line == 5:
      print('*' * 5)
    else:
      print('*' + ' ' * 3 + '*')


choise = int(input('Что рисуем? 1 - треугольник, 2 - прямоугольник '))
if choise == 1:
    triangle()
elif choise == 2:
    rectangle()
else:
    print('Ошибка ввода!')