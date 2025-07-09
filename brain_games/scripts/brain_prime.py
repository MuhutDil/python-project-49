from brain_games.game_basis import game
from brain_games.games.prime import (
    answer_to_question,
    generate_question,
    rule,
)


def main():
    game(rule=rule,
         generate_question=generate_question,
         answer_to_question=answer_to_question)


if __name__ == "__main__":
    main()