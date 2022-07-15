import random
import operator
MANUAL = 'What is the result of the expression?'


def get_question_and_answer():
    first_number = random.randint(1, 20)
    second_number = random.randint(1, 20)
    signs = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }
    sign = random.choice(list(signs.keys()))
    question = f"{first_number} {sign} {second_number}"
    answer = str(signs[sign](first_number, second_number))
    return question, answer
