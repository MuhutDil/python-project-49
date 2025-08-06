"""Brain Games Engine - Is simple quiz-style games.
 
This module provides the core functionality for interactive quiz games where
users answer questions and receive feedback on their performance.
"""


import prompt

MAX_CORRECT_ANSWERS = 3


def game(rule, question_and_answer):
    """Main game engine that orchestrates the quiz gameplay.
    
    Args:
        rule: Function that displays the game rules/instructions.
        question_and_answer: Function that generates a question
            and correct answer to the current question
        
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
    print(rule)
    for _ in range(MAX_CORRECT_ANSWERS):
        question, correct_answer = question_and_answer()
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
