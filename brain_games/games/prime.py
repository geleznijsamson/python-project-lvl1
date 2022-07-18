from random import randint


MANUAL = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(question):
    if question != 2 and question % 2 == 0 or question <= 1:
        return False
    else:
        div = 3
        while div <= question // 2:
            if question % div == 0:
                return False
            div += 2
        return True


def get_question_and_answer():
    question = randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return question, answer
