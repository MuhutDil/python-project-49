from brain_games.game_basis import game
from brain_games.games.progression import (
    RULE,
    question_and_answer,
)


def main():
    game(
        rule=RULE,
        question_and_answer=question_and_answer,
        )


if __name__ == "__main__":
    main()