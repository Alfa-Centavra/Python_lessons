#n школьников делят k мандаринов поровну, неделящийся остаток остается в корзине. Сколько целых мандаринов достанется каждому школьнику? Сколько целых мандаринов останется в корзине?
#На вход программе подаётся два целых числа: количество школьников и количество мандаринов, каждое на отдельной строке.
# put your python code here

n = int(input())
k = int(input())

print(k // n)
print(k % n)