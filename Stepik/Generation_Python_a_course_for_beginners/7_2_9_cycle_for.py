#На вход программе подается натуральное число n, а затем n различных натуральных чисел, каждое на отдельной строке. Напишите программу, которая выводит наибольшее и второе наибольшее число последовательности.
n = int(input())
largest = 0
sec_l = 1
for i in range(1, n + 1):
    num = int(input())
    if num > largest:
        sec_l = largest
        largest = num
    elif num > sec_l:
        sec_l = num
print(largest)
print(sec_l)