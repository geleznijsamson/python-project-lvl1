import random
head = 'What is the result of the expression?'


def calculation():
    signs = ['+', '-', '*']
    a = str(random.randint(1, 100))
    b = random.choice(signs)
    c = str(random.randint(1, 100))
    question = a + b + c
    print(f'Question: {question}')
    if b == '+':
        return str(int(a) + int(c))
    elif b == '-':
        return str(int(a) - int(c))
    else:
        return str(int(a) * int(c))
