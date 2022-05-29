import random


def get_jokes(count_j):
    """
    :param count_j: accepts the required number of jokes
    :return: returns the specified number of jokes in a list
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    for n in range(count_j):
        jokes.append(f'{nouns[random.randint(0,4)]} {adverbs[random.randint(0,4)]} {adjectives[random.randint(0,4)]}')

    return jokes

count_j = int(input("Введите количество шуток: "))
print(f'Полученные шутки:  \n {get_jokes(count_j)}')
