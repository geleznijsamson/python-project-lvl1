from brain_games import greet


def structure(game, head):
    user_name = greet.greeting(head)
    i = 0
    while i < 3:
        correct_answer = game
        answer = input('Your answer: ')
        i += 1
        if answer == correct_answer:
            print('Correct')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
