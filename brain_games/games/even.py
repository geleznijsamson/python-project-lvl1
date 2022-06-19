from brain_games import greet
from brain_games import logic
from random import randint


def even_game():
    greet.greeting()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(0, 3):
        x = randint(1, 100)
        if x % 2 == 0:
            y = 'yes'
            logic.structure(x, y)
        elif x % 2 != 0:
            y = 'no'
            logic.structure(x, y)
    print('Congratulation!')
