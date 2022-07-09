from random import randint
manual = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)
    count = 0
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            count += 1
    answer = 'yes' if count <= 0 else 'no'
    return question, answer
