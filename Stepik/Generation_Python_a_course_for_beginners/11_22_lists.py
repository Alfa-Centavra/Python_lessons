#На вход программе подается строка текста, содержащая целые числа. Из данной строки формируется список чисел. Напишите программу, которая сортирует и выводит данный список сначала по возрастанию, а затем по убыванию. 
# put your python code here
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
numbers.sort()
print(*numbers)
numbers.sort(reverse=True)
print(*numbers)
