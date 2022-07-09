from brain_games import engine
from brain_games.games.progression import get_question_and_answer
from brain_games.games.progression import manual


def main():
    engine.play_game(get_question_and_answer, manual)
