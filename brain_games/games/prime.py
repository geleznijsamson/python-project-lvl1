from random import randint
from sympy import isprime


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if isprime(question) else 'no'
    return question, answer
