"""Even/Odd Number Game Module.
 
This module provides functionality for a simple game where users must determine
whether a randomly generated number is even or odd. It includes functions to:
- Generate random numbers
- Check even/odd status
- Format game responses
 
The main interface is the generate_game_conditions() function
which returns a tuple of (question, correct_answer).
"""
import random

RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game_conditions():
    """Generate a random number question and its correct answer.
    
    This is the main game function that coordinates:
    1. Question generation
    2. Answer determination
    
    Returns:
        tuple: A (question, answer) pair where:
            - question (int): Random number between 1-100
            - answer (str): 'yes' if even, 'no' if odd
    """
    question = random.randint(1, 100)  # NOSONAR
    correct_answer = convert_to_answer(question)
    return question, correct_answer


def is_even(num):
    """Determines if a number is even.
    
    Args:
        num (int): The number to check
    
    Returns:
        bool: True if the number is even, False if odd
    """
    return True if num % 2 == 0 else False


def convert_to_answer(question):
    """Convert numeric question to game answer string.
    
    Args:
        question (int): The number to evaluate
    
    Returns:
        str: 'yes' if question is even, 'no' if odd
    """
    return {True: 'yes', False: 'no'}[is_even(question)]
