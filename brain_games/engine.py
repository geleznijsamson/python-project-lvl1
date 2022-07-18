from prompt import string


def play_game(get_question_and_answer, manual):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!')
    print(manual)
    number_of_rounds = 3
    for i in range(number_of_rounds):
        question, answer = get_question_and_answer()
        print(f'Question: {question}')
        user_answer = input('Your answer: ')
        if user_answer != answer:
            print(f""
                  f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')
