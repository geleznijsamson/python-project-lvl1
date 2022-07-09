from prompt import string


def greet():
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def play_game(get_question_and_answer, manual):
    user_name = greet()
    print(manual)
    i = 0
    while i < 3:
        [question, answer] = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer == answer:
            print('Correct!')
            i += 1
        else:
            print(f""
                  f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'.\n"
                  f"Let's try again, {user_name}!")
            return
    print(f'Congratulations, {user_name}!')
