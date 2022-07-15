from random import randint
MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_for_simplicity(question):
    for i in range(2, question // 2 + 1):
        return question % i == 0


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'no' if check_for_simplicity(question) else 'yes'
    return question, answer
