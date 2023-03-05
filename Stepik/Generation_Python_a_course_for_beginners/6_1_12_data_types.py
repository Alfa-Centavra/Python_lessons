#Даны названия трех городов. Напишите программу, которая определяет самое короткое и самое длинное название города.
a = input()
b = input()
c = input()
a1 = len(a)
b1 = len(b)
c1 = len(c)

if a1 > b1 > c1:
    print(c)
    print(a)
elif a1 > c1 > b1:
    print(b)    
    print(a) 
elif b1 > a1 > c1:
    print(c)
    print(b)
elif b1 > c1 > a1:
    print(a)
    print(b)
elif c1 > b1 > a1:
    print(a)
    print(c)
else:
    print(b)
    print(c)
