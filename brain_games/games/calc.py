import random
import operator
manual = 'What is the result of the expression?'


def get_question_and_answer():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    signs = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
    }

    sign = random.choice(list(signs.keys()))
    question = str(number_1) + ' ' + str(sign) + ' ' + str(number_2)
    answer = str(signs[sign](number_1, number_2))
    return question, answer
