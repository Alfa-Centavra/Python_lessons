#Напишите функцию draw_box(), которая выводит звездный прямоугольник с размерами 14×10 в соответствии с образцом:
# объявление функции
def draw_box():
    print('*' * 10)
    for i in range(2, 14):
        print('*', ' ' * 6, '*')
    print('*' * 10)

# основная программа
draw_box()  # вызов функции