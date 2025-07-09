"""Even Number Checker Module.
 
This module generates random numbers and checks whether they are even or odd.
It's designed for quiz systems where users
need to determine if a number is even.
 
The module provides:
- Random number generation (1-100)
- Even/odd checking
- Consistent answer storage between question generation and verification
 
Global Variables:
    ANSWER (int|None): Stores the last generated number. Initialized as None.
 
Functions:
    rule(): Prints the game instructions.
    generate_question(): Generates a random number question.
    is_even(num): Checks if a number is even.
    answer_to_question(): Returns the correct answer ('yes' or 'no').
"""
import random

ANSWER = None


def rule():
    """Prints the game instructions.
    
    Explains to the user what they should do with the generated numbers.
    """
    print('Answer "yes" if the number is even, otherwise answer "no".')


def generate_question():
    """Generates a random number question.
    
    Generates a random integer between 1 and 100
    and stores it in the global ANSWER.
    
    Returns:
        int: The generated number
    """
    num = random.randint(1, 100)  # NOSONAR
    global ANSWER
    ANSWER = num
    return num


def is_even(num):
    """Determines if a number is even.
    
    Args:
        num (int): The number to check
    
    Returns:
        bool: True if the number is even, False if odd
    """
    return True if num % 2 == 0 else False


def answer_to_question():
    """Provides the correct answer to the last generated question.
    
    Converts the boolean result from is_even() into 'yes' or 'no'.
    
    Returns:
        str: 'yes' if the number is even, 'no' if odd
    """
    return {True: 'yes', False: 'no'}[is_even(ANSWER)]
