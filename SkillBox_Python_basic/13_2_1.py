def calculate_tax(price, tax):
    total = price + (price * tax / 100)
    print(total)
    return

myPrice = float(input('Введите цену: '))
myTax = int(input('Введите налог (в %): '))



totalPrice = calculate_tax(myPrice, myTax)

newTax = int(input('Введите новый налог (в %): '))

totalPrice = calculate_tax(totalPrice, newTax)

print('Итоговая цена:', totalPrice)