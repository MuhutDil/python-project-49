"""Brain Games Engine - Is simple quiz-style games.
 
This module provides the core functionality for interactive quiz games where
users answer questions and receive feedback on their performance.
"""


import prompt

MAX_CORRECT_ANSWERS = 3


def welcome_user():
    """Welcome the user and collect their name.
    
    Returns:
        str: The name entered by the user after displaying welcome messages.
        
    Displays:
        - Welcome banner
        - Prompt for user's name
        - Personalized greeting
    """
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    """Present a question to the user and collect their answer.
    
    Args:
        question: The question text to display to the user.
        
    Returns:
        str: The user's answer to the question.
        
    Displays:
        - Formatted question (prefixed with 'Question:')
        - Answer prompt
    """
    print(f'Question: {question}')
    return prompt.string('Your answer: ')


def endind_game(name, status_game, *, answer_data):
    """Display the game ending message with appropriate feedback.
    
    Args:
        name: The user's name for personalization.
        status_game: Boolean indicating if the user won (True) or lost (False).
        answer_data: Dictionary containing:
            - user_answer: The incorrect answer provided by the user
            - correct_answer: The right answer
            
    Displays:
        - Congratulatory message if won
        - Failed attempt message with correct answer if lose
    """
    if status_game:
        print(f'Congratulations, {name}!')
    else:
        print(
            f"'{answer_data['user_answer']}' is wrong answer ;(."
            f"Correct answer was '{answer_data['correct_answer']}'.\n"
            f"Let's try again, {name}!"
        )


def game(rule, generate_question, answer_to_question):
    """Main game engine that orchestrates the quiz gameplay.
    
    Args:
        rule: Function that displays the game rules/instructions.
        generate_question: Function that generates a new question.
        answer_to_question: Function that provides the correct answer
                            to the current question.
        
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
    name = welcome_user()
    rule()
    correct_answers = 0
    status_game = True
    answer_data = {}
    while correct_answers < MAX_CORRECT_ANSWERS:
        question = generate_question()
        user_answer = ask_question(question)
        correct_answer = answer_to_question()
        if correct_answer == user_answer:
            correct_answers += 1
        else:
            status_game = False
            answer_data['user_answer'] = user_answer
            answer_data['correct_answer'] = correct_answer
            break
    endind_game(name, status_game, answer_data=answer_data) 
