#Программа должна вывести n-ый член геометрической прогрессии.
# put your python code here
b = int(input('Введите число: '))
q = int(input('Введите число: '))
n = int(input('Введите число: '))

print(b * (q ** (n - 1)))
