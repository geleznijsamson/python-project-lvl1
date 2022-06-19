def structure(x, y):
    print(f'Question: {x}')
    answer = input('Your answer: ')
    if answer == y:
        print('Correct')
    else:
        print(f"'{answer}' is wrong answer ;(. Correct answer was '{y}'.\n"
              f"Let's try again!")
