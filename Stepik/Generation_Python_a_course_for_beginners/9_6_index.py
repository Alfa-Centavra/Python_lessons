#На вход программе подается одна строка. Напишите программу, которая определяет сколько раз в строке встречаются символы + и *.
# put your python code here
s = input()
count_1 = 0
count_2 = 0
for i in range(len(s)):
    if s[i] in '+':
        count_1 += 1
    
    if s[i] in '*':
        count_2 += 1
    
print('Символ + встречается', count_1, 'раз')
print('Символ * встречается', count_2, 'раз')