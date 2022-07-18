from random import randint
from math import gcd


MANUAL = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_1 = randint(1, 100)
    number_2 = randint(1, 100)
    question = f"{number_1} {number_2}"
    answer = str(gcd(number_1, number_2))
    return question, answer
