#Напишите функцию get_month(language, number), которая принимает на вход два аргумента language – язык ru или en и number – номер месяца (от 1 до 12) и возвращает название месяца на русском или английском языке.

# объявление функции
def get_month(language, number):
    en = ['', 'january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    ru = ['', 'январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']

    if language == 'ru':
        return ru[number]
    else:
        return en[number]
            

# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))