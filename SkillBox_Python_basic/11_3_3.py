print('Задача 1. Космические рейнджеры')
#В далеком (а может и не очень) будущем на некоторой планете можно купить космический корабль за пол-кредита (CR). Один CR это 2200 чатлов. Причем чатлы неделимы и являются всегда целым числом. Напишите простую программу-конвертор валют. В программу вводится количество чатлов, а она сообщает сколько это CR и сколько кораблей можно купить на эту сумму.

chatl = int(input('Сколько чатлов? '))

cr = 2200
print('Это:', chatl / cr, 'CR')

ship = int(chatl / (cr * 0.5))
print('Можно купить кораблей:', ship)