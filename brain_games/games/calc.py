import random
head = 'What is the result of the expression?'


def calculate():
    signs = ['+', '-', '*']
    number_1 = str(random.randint(1, 100))
    sign = random.choice(signs)
    number_2 = str(random.randint(1, 100))
    question = number_1 + sign + number_2
    print(f'Question: {question}')
    if sign == '+':
        return str(int(number_1) + int(number_2))
    elif sign == '-':
        return str(int(number_1) - int(number_2))
    else:
        return str(int(number_1) * int(number_2))
