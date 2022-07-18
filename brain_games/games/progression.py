from random import randint


MANUAL = 'What number is missing in the progression?'


def get_question_and_answer():
    first_number = randint(1, 50)
    interval = randint(1, 5)
    progression_length = 10
    stop = first_number + interval * progression_length
    progression = list(range(first_number, stop, interval))
    index_to_change = randint(0, progression_length - 1)
    answer = str(progression[index_to_change])
    question = ' '.join(map(str, progression)).replace(answer, '..')
    return question, answer

