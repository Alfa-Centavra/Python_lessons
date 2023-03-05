#Панграмма – это фраза, содержащая в себе все буквы алфавита. Обычно панграммы используют для презентации шрифтов, чтобы можно было в одной фразе рассмотреть все глифы.

#Напишите функцию, is_pangram(text) которая принимает в качестве аргумента строку текста на английском языке и возвращает значение True если текст является панграммой и False в противном случае.


#print(is_pangram('Jackdaws love my big sphinx of quartz'))          True
#print(is_pangram('The jay pig fox zebra and my wolves quack'))      True
#print(is_pangram('Hello world'))                                    False

# объявление функции
def is_pangram(text):
    alphabet = [chr(char) for char in range(97, 123)]
    for char in alphabet:
        if char not in text.lower():
            return False
    return True

# считываем данные
text = input()

# вызываем функцию
print(is_pangram(text))