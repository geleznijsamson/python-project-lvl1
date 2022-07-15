from random import randint
MANUAL = 'What number is missing in the progression?'


def get_question_and_answer():
    first_number = randint(1, 50)
    interval = randint(1, 5)
    stop = first_number + interval * 10
    progression = list(range(first_number, stop, interval))
    index = randint(0, len(progression) - 1)
    answer = str(progression[index])
    progression[index] = '..'
    question = ' '.join(map(str, progression))
    return question, answer
