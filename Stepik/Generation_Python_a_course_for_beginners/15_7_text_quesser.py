#Угадайка слов
from random import choice, randrange

word_list = ['год', 'человек', 'время', 'дело', 'жизнь', 'день', 'рука', 'раз', 'работа', 'слово', 'место', 'лицо', 'друг', 'глаз', 'вопрос', 'дом', 'сторона', 'страна', 'мир', 'случай', 'голова', 'ребёнок', 'сила', 'конец', 'вид', 'система', 'часть', 'город', 'отношение', 'женщина', 'деньги', 'земля', 'машина', 'вода', 'отец', 'проблема', 'час', 'право', 'нога', 'решение', 'дверь', 'образ', 'история', 'власть', 'закон', 'война', 'бог', 'голос', 'тысяча', 'книга', 'возможность', 'результат', 'ночь', 'стол', 'имя', 'область', 'статья', 'число', 'компания', 'народ', 'жена', 'группа']
letters = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
used_words = list()

def get_word(list_of_words: list) -> str:
    while True:
        new_word = choice(list_of_words).upper()
        if new_word in used_words:
            continue
        else:
            used_words.append(new_word)
            return new_word
            
def user_input() -> str:
    while True:
        print(' Загадайте слово.')
        print()
        new_word = input(' --> ').upper()
        wrong_word = False
        for l in new_word:
            if l not in letters:
                wrong_word = True
                break
        if new_word in used_words:
            print(' Такое слово уже было.')
            print()
            continue
        elif wrong_word:
            print(' Слово должно состоять только из посконных, скрепных, великорусских букв!')
            print()
            continue
        else:
            used_words.append(new_word)
            print('\n' * 100)
            return new_word

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word: str):
    word_on_screen = ['_' for i in range(len(word))]
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print(display_hangman(tries))
    print()
    print('Загаданное слово:')
    print()
    print(' ', *word_on_screen)
    print()
    #print('Test: ', word) # test
    while not guessed:
        print(' Назовите букву или слово целиком.')
        print()
        guess = input(' --> ').upper()
        if guess == word:
            print(' Поздравляю, вы победили!')
            print()
            guessed = True
        elif len(guess) == 1 and guess in word and guess not in guessed_letters:
            print(' Есть такая буква!')
            print()
            guessed_letters.append(guess)
            for i, el in enumerate(word):
                if el == guess:
                    word_on_screen[i] = el
            print(' ', *word_on_screen)
            print()
            if '_' not in word_on_screen:
                print(' Поздравляю, вы победили!')
                print()
                guessed = True
            else:
                print(' Уже назывались буквы: ', *guessed_letters)
                print()
        elif guess in guessed_letters:
            print(' Вы уже называли эту букву.')
            print()
            print(' ', *word_on_screen)
            print()
            print(' Уже назывались буквы: ', *guessed_letters)
            print()
        elif len(guess) == 1 and guess not in word:
            if guess in letters:
                tries -= 1
                guessed_letters.append(guess)
                print(' К сожалению вы не угадали!')
                print()
                print(display_hangman(tries))
                print()
                print(' ', *word_on_screen)
                print()
                if tries == 0:
                    print(' К сожалению вы проиграли.')
                    print()
                    print(' Это было слово', word)
                    print()
                    guessed = True
                else:
                    print(' Уже назывались буквы: ', *guessed_letters)
                    print()
            else:
                print(' Нет такой буквы в этом слове. Да и в русском алфавите тоже.')
                print()
                print(' ', *word_on_screen)
                print()
                print(' Уже назывались буквы: ', *guessed_letters)
                print()
        elif len(guess) != 1 and guess != word:
            if word in guessed_words:
                print(' Вы уже называли это слово.')
                print()
                print(' ', *word_on_screen)
                print()
                print(' Уже назывались буквы: ', *guessed_letters)
                print()
            else:
                tries -= 1
                guessed_words.append(guess)
                print(' К сожалению вы не угадали!')
                print()
                print(display_hangman(tries))
                print()
                print(' ', *word_on_screen)
                print()
                if tries == 0:
                    print(' К сожалению вы проиграли.')
                    print()
                    print(' Это было слово', word)
                    print()
                    guessed = True
                else:
                    print(' Уже назывались буквы: ', *guessed_letters)
                    print()
        
        
def get_answer(question: str, variants_of_answers: list) -> int:
    while True:
        print(' ', question)
        print()
        for i in range(len(variants_of_answers)):
            print(' ', i, '-', variants_of_answers[i])
            print()
        answer = input('--> ')
        print()
        if answer.isdecimal() and int(answer) in range(len(variants_of_answers)):
            return int(answer)
        else:
            print(' Не совсем понятен ваш выбор.')
            print()
            continue


print(' Давайте сыграем в "Виселицу"!')
print()

if get_answer(' С кем вы хотите сыграть?', [' с искусственным интеллектом.', ' с человеком.']):
    second_player_man = True
else:
    second_player_man = False

while True:
    if second_player_man:
        play(user_input())
    else:
        play(get_word(word_list))
    
    if not get_answer(' Хотите сыграть еще?', ['нет', 'да']):
        print(' Всего доброго!')
        print()
        break