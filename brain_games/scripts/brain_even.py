from brain_games.engine import play_game
from brain_games.games.even import get_question_and_answer
from brain_games.games.even import MANUAL


def main():
    play_game(get_question_and_answer, MANUAL)
