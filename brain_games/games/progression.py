import random
head = 'What number is missing in the progression?'


def create_a_list():
    number = random.randint(1, 50)
    interval = random.randint(1, 5)
    stop = number + interval * 10
    progression = list(range(number, stop, interval))
    return progression


def calculate():
    progression = create_a_list()
    index = random.choice(progression)
    string = str(progression).strip()[1:-1].replace(',', '')
    question = string.replace(str(index), '..')
    print(f"Question: {question}")
    return str(index)
