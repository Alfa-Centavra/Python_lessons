bet = int(input('Сколько ставим? '))
coefficient = float(input('Какой коэффициент? '))

win = round(bet * coefficient, 2)

print('Потенциальный выигрыш: ', win)