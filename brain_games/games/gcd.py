from random import randint
from math import gcd
head = 'Find the greatest common divisor of given numbers.'


def calculation():
    a = randint(1, 100)
    b = randint(1, 100)
    question = str(a) + ' ' + str(b)
    print(f'Question: {question}')
    return str(gcd(a, b))
