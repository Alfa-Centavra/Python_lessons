#Напишите программу для робота-начальника. Он спрашивает у пользователя, выполнил ли он задание, которое выдавал вчера, и продолжает это делать до тех пор, пока тот не ответит ему “Да, конечно, сделал”.

quest = input('Выполнили ли вы задание? ').capitalize()
while quest != 'Да, конечно, сделал':
  quest = input('Выполнили ли вы задание? ').capitalize()
print('Отлично!')
