print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')


def separator():
    print('------------------------------------------')


def main_menu():
    separator()
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')


def submenu_edit_info():
    separator()
    print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
    print('1 - Общая информация')
    print('2 - Информация о предпринимателе')
    print('0 - Назад')


def submenu_print_info():
    separator()
    print('ВЫВЕСТИ ИНФОРМАЦИЮ')
    print('1 - Общая информация')
    print('2 - Вся информация')
    print('0 - Назад')


def general_info_user(name_parameter, age_parameter, phone_parameter,
                      email_parameter, index_parameter, adres_parameter,
                      anything_parameter):
    separator()
    print('Имя:    ', name_parameter)
    if 11 <= age_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif age_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= age_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'
    print('Возраст:', age_parameter, years_parameter)
    print('Телефон:', phone_parameter)
    print('E-mail: ', email_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес: ', adres_parameter)
    if anything:
        print('')
        print('Дополнительная информация:')
        print(anything_parameter)


def entrepreneur_info_user(ogrnip_parametr, inn_parametr,
                           checking_account_parametr,
                           bank_name_parametr, bik_parametr,
                           correspondent_account_parametr):
    print()
    print('Информация о предпринимателе')
    print('ОГРНИП:', ogrnip_parametr)
    print('ИНН:', inn_parametr)
    print('Банковские реквизиты')
    print('Р/с:', checking_account_parametr)
    print('Банк:', bank_name_parametr)
    print('БИК:', bik_parametr)
    print('К/с', correspondent_account_parametr)


while True:
    # main menu
    main_menu()
    choise = int(input('Введите номер пункта меню: '))
    if choise == 0:
        break

    elif choise == 1:
        submenu_edit_info()
        choise = int(input('Введите номер пункта меню: '))
        if choise == 0:
            main_menu()
        elif choise == 1:
            # input general info
            name_person = input('Введите имя: ')
            # validate user age
            age = int(input('Введите возраст: '))
            if age < 0:
                print('Возраст должен быть положительным')
                age = int(input('Введите возраст: '))

            update_phone = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
            phone = ''
            for choise_number in update_phone:
                if choise_number == '+' or ('0' <= choise_number <= '9'):
                    phone += choise_number
            email = input('Введите адрес электронной почты: ')
            while '@' not in email and '.' not in email:
                print('Почта должна содержать "@" и ".", попробуйте ещё раз!')
                email = input('Введите адрес электронной почты: ')
            index = input('Введите почтовый индекс: ')
            index_number = ''
            for index_choise in index:
                if '0' <= index_choise <= '9':
                    index_number += index_choise
                index = index_number
            adres = input('Введите почтовый адрес (без индекса): ')
            anything = input('Введите дополнительную информацию:\n')

        elif choise == 2:
            while 1:
                ogrnip = int(input('Введите ОГРНИП: '))
                ogrnip_count = 0
                num = ogrnip
                while num != 0:
                    ogrnip_count += 1
                    num //= 10
                if ogrnip_count == 15:
                    break
                print('ОГРНИП должен содержать 15 цифр')

            inn = int(input('Введите ИНН: '))
            while 1:
                checking_account = int(input('Введите расчетный счет: '))
                checking_account_count = 0
                num = ogrnip
                while num != 0:
                    checking_account_count += 1
                    num //= 10
                if checking_account_count == 15:
                    break
                print('Pасчетный счет должен содержать 20 цифр')
            bank_name = input('Введите название банка: ')
            bik = int(input('Введите БИК: '))
            print('Введите корреспондентский счёт: ', end='')
            correspondent_account = int(input())

        else:
            print('Введите корректный пункт меню')

    elif choise == 2:
        submenu_print_info()
        choise = int(input('Введите номер пункта меню: '))
        if choise == 0:
            main_menu()
        elif choise == 1:
            general_info_user(name_person, age,
                              phone, email, index, adres,
                              anything)
        elif choise == 2:
            general_info_user(name_person, age,
                              phone, email, index, adres,
                              anything)
            entrepreneur_info_user(ogrnip, inn,
                                   checking_account, bank_name,
                                   bik, correspondent_account)
        else:
            print('Введите корректный пункт меню')

    else:
        print('Введите корректный пункт меню')
