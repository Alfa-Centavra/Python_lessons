print('Задача 1. Опять налоги')
#У правительства одной из стран есть бухгалтерская программа, которая суммирует налоги её граждан, компаний плюс НДС с товаров.
#Cтрана развивалась, суммарные налоги увеличивались, и бухгалтеры заметили, что после добавления к общей сумме налогов некого НДС 
#от какого-то продукта общая сумма перестала меняться…
#Нужно помочь бухгалтерам: напишите функцию, на вход которой подаются два числа — общая сумма налога tax и новый налог new_tax,
#который нужно добавить к общей сумме. Функция должна проверять, возможно ли сложить эти два числа или нет,
#и выводить соответствующее сообщение о том, увеличится ли бюджет или нет.
#Пример 1:
#Введите бюджет страны: 1.23e2
#Новые поступления (налог): 1.2e1
#Результат: Бюджет увеличится

#Пример 2:
#Введите бюджет страны: 1.231221200034e12
#Новые поступления (налог): 1.2e-4
#Результат: Бюджет не изменится
def tax_new_tax():
    tax = float(input('Введите бюджет страны: '))
    new_tax = float(input('Новые поступления (налог): '))
    summ = tax + new_tax
    if abs(summ - tax - new_tax) < 1e-15:
        print('Результат: Бюджет увеличится')
    else:
        print('Результат: Бюджет не изменится')

tax_new_tax()