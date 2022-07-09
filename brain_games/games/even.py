from random import randint
manual = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'no' if question % 2 else 'yes'
    return question, answer
