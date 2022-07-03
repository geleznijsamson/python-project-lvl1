from random import randint
head = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def calculate():
    question = randint(1, 100)
    print(f'Question: {question}')
    count = 0
    for i in range(2, question // 2 + 1):
        if question % i == 0:
            count += 1
    if count <= 0:
        return 'yes'
    else:
        return 'no'
