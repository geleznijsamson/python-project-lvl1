from random import randint
head = 'Answer "yes" if the number is even, otherwise answer "no".'


def calculate():
    question = randint(1, 100)
    print(f'Question: {question}')
    if question % 2 == 0:
        return 'yes'
    else:
        return 'no'
