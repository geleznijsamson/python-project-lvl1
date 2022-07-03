from brain_games import engine
from brain_games.games.prime import calculate
from brain_games.games.prime import head


def main():
    engine.play_game(calculate, head)


if __name__ == '__main__':
    main()