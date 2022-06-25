from prompt import string


def greeting(head):
    print('Welcome to the Brain Games!')
    name = string('May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{head}')
    return name
