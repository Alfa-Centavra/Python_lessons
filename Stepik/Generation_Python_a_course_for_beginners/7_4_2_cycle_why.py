#На вход программе подается последовательность целых чисел от 1 до 5, характеризующее оценку ученика, каждое число на отдельной строке. Концом последовательности является любое отрицательное число, либо число большее 5. Напишите программу, которая выводит количество пятерок.
num = int(input())
count = 0
while num > 0 and num <= 5:
    
    if num == 5:
        count += 1
    num = int(input())
print(count)