from random import randint


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def check_for_simplicity(question):
    count = 0
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            count += 1
    return count <= 0


def get_question_and_answer():
    question = randint(2, 100)
    answer = 'yes' if check_for_simplicity(question) else 'no'
    return question, answer
