import prompt
import random


def game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        x = random.randint(1, 100)
        print(f'Question: {x}')
        answer = prompt.string('Your answer: ')
        i += 1
        if (x % 2 == 0 and answer == 'yes') or (x % 2 != 0 and answer == 'no'):
            print('Correct!')
            continue
        else:
            if answer == 'yes':
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\
                Let's try again, {name}!")
            elif answer == 'no':
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\
                Let's try again, {name}!")
            else:
                print(f"'{answer}' is wrong answer.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
