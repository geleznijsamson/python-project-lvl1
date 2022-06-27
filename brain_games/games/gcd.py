from random import randint
from math import gcd
head = 'Find the greatest common divisor of given numbers.'


def calculate():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = str(number_1) + ' ' + str(number_2)
    print(f'Question: {question}')
    return str(gcd(number_1, number_2))
