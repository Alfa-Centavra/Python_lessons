#На вход программе подается строка текста. Напишите программу, которая подсчитывает количество цифр в данной строке.
# put your python code here
s = input()
count = 0
for i in range(10):
    count += s.count(str(i))
print(count)