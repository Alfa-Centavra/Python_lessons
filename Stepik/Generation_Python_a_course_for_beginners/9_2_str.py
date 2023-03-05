#На вход программе подается строка. Напишите программу, которая подсчитывает количество буквенных символов в нижнем регистре.
# put your python code here
s = input()
l = s.upper()
count = 0
for i in range(len(s)):
    if s[i] != l[i]:
        count += 1
print(count)