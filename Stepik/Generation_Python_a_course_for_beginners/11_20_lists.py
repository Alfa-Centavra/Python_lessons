#На вход программе подается строка, содержащая английский текст. Напишите программу, которая подсчитывает общее количество артиклей: 'a', 'an', 'the'.
#William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.
#Общее количество артиклей: 7

# put your python code here
s = input()
l = s.lower().split()
cnt1 = l.count('a')
cnt2 = l.count('an')
cnt3 = l.count('the')
a = cnt1 + cnt2 + cnt3
print('Общее количество артиклей:', a)