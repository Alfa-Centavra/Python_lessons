#Напишите программу, выводящую следующий список: ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]
sp = list()
for i in range(26):
    sp.append(chr(ord('a') + i)*(i+1))
print(sp)