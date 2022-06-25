from brain_games import greet
import random
head = 'What is the result of the expression?'


def calc_game():
    user_name = greet.greeting(head)
    i = 0
    while i < 3:
        signs = ['+', '-', '*']
        random.shuffle(signs)
        a = str(random.randint(1, 100))
        b = random.choice(signs)
        c = str(random.randint(1, 100))
        question = a + b + c
        if b == '+':
            correct_answer = int(a) + int(c)
        elif b == '-':
            correct_answer = int(a) - int(c)
        else:
            correct_answer = int(a) * int(c)
        print(f'Question: {question}')
        answer = input('Your answer: ')
        i += 1
        if answer == str(correct_answer):
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
