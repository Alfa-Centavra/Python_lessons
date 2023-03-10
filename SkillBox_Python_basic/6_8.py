print('Задача 8. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.
 
# Напишите программу, 
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.
 
# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.

# Подсказка: используйте бинарный поиск, а не конкатенацию.
num = int(input('Загадайте число между 1 и 100: '))

start = 1
end = 100
n = (start + end) // 2
while 1 < num <= 100:
  print(n)
  tab = int(input('Твое число равно, меньше или больше, чем число N? '))
  if tab == 3:
    end = n
    n -= 1
    n = (start + end) // 2
    
  elif tab == 2:
    start = n
    n += 1
    n = (start + end) // 2
    
  elif tab == 1:
    print('Я угадал число!')
    break
    
    