from brain_games import greeting


def play_game(calculate, head):
    user_name = greeting.greet(head)
    i = 0
    while i < 3:
        correct_answer = calculate()
        answer = input('Your answer: ')
        i += 1
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f""
                  f"'{answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
