"""Brain Games Engine - Is simple quiz-style games.
 
This module provides the core functionality for interactive quiz games where
users answer questions and receive feedback on their performance.
"""


import prompt

MAX_CORRECT_ANSWERS = 3


def launch_game(game):
    """Main game engine that orchestrates the quiz gameplay.
    
    Args:
        game: Module containing game logic with:
            - RULE: str (game rules)
            - generate_game_conditions(): -> tuple(question, correct_answer)
        
    Workflow:
        1. Welcomes the user
        2. Displays game rules
        3. Start asking questions, the number of which is limited
           in the constant MAX_CORRECT_ANSWERS:
            - Generates question
            - Gets user answer
            - Checks correctness
        4. Ends game with appropriate message
        
    Note:
        The game ends early if the user answers incorrectly.
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.RULE)
    for _ in range(MAX_CORRECT_ANSWERS):
        question, correct_answer = game.generate_game_conditions()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer != correct_answer:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'.\n"
                f"Let's try again, {name}!"
            )
            break
    else:
        print(f'Congratulations, {name}!')
