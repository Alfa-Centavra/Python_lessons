#На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит его в двоичную, восьмеричную и шестнадцатеричную системы счисления.

# put your python code here
a = int(input())

bin_num = bin(a)  
oct_num = oct(a)  
hex_num = hex(a)  

print(bin_num[2:]) 
print(oct_num[2:]) 
print(hex_num[2:].upper()) 



