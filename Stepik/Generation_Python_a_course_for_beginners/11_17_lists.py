#На вход программе подается строка текста, содержащая натуральные числа. Из данной строки формируется список чисел. Напишите программу, которая подсчитывает, сколько в полученном списке пар элементов, равных друг другу. Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# put your python code here
n = input().split()
count = 0
for i in range(len(n)):
   
    for j in range(i + 1, len(n)):
        if n[i] == n[j]:
            count += 1
print(count)