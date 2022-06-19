from brain_games import greet
from brain_games import logic
from random import randint


def even_game():
    greet.greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        x = randint(1, 100)
        i += 1
        if x % 2 == 0:
            y = 'yes'
            logic.structure(x, y)
            continue
        elif x % 2 != 0:
            y = 'no'
            logic.structure(x, y)
            continue
        else:
            y = True
            logic.structure(x, y)
            return
    print('Congratulation!')
