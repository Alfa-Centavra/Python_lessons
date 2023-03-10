#Магический шар
from random import choice

answers = [
    'Бесспорно',
    'Предрешено',
    'Никаких сомнений',
    'Определённо да',
    'Можешь быть уверен в этом',
    'Мне кажется - да',
    'Вероятнее всего',
    'Хорошие перспективы',
    'Знаки говорят - да',
    'Да',
    'Пока неясно, попробуй снова',
    'Спроси позже',
    'Лучше не рассказывать',
    'Сейчас нельзя предсказать',
    'Сконцентрируйся и спроси опять',
    'Даже не думай',
    'Мой ответ - нет',
    'По моим данным - нет',
    'Перспективы не очень хорошие',
    'Весьма сомнительно'
]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
name = input('Как тебя зовут? ')
print(f'Привет, {name}.')

game = 'да'
while game == 'да':
    print('О чем ты хочешь спросить?')
    input()
    print(choice(answers))
    print()
    game = input('Если хочешь задать вопрос, просто скажи "да": ')

print()
print('Возвращайся, если возникнут вопросы!')
print()