#Напишите программу, которая принимает три положительных числа и определяет вид треугольника, длины сторон которого равны введенным числам.
#На вход программе подаются три числа – длины сторон существующего треугольника
#Программа должна вывести на экран текст – вид треугольника («Равносторонний», «Равнобедренный» или «Разносторонний»).

a = int(input())
b = int(input())
c = int(input())
if a == b == c:
    print('Равносторонний')
elif a == b != c or a != b == c or a == c != b:
    print('Равнобедренный')
else:
    print('Разносторонний')