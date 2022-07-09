import random
manual = 'What number is missing in the progression?'


def create_a_list():
    number = random.randint(1, 50)
    interval = random.randint(1, 5)
    stop = number + interval * 10
    progression = list(range(number, stop, interval))
    return progression


def get_question_and_answer():
    progression = create_a_list()
    index = random.randint(0, len(progression) - 1)
    answer = progression[index]
    new_index = '..'
    progression[index] = new_index
    question = str(progression).strip('[]').replace(',', '').replace("'", "")
    return question, str(answer)
