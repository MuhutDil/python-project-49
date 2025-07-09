"""Prime Number Checker Module.
 
This module generates random numbers and checks their primality. 
It's designed for quiz systems where users
need to determine if a number is prime.
 
The module provides:
- Random number generation (1-100)
- Primality checking
- Consistent answer storage between question generation and verification
 
Global Variables:
    ANSWER (int|None): Stores the last generated number. Initialized as None.
 
Functions:
    rule(): Prints the game instructions.
    generate_question(): Generates a random number question.
    is_prime(num): Checks if a number is prime.
    answer_to_question(): Returns the correct answer ('yes' or 'no').
"""
import random

ANSWER = None


def rule():
    """Prints the game instructions.
    
    Explains to the user what they should determine about the number.
    """
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


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


def is_prime(num):
    """Determines if a number is prime.
    
    Args:
        num (int): The number to check (1 <= num <= 100)
    
    Returns:
        bool: True if the number is prime, False otherwise
    """
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    upper_limit = int(num ** 0.5) + 1
    for i in range(3, upper_limit, 2):
        if num % i == 0:
            return False
    return True


def answer_to_question():
    """Provides the correct answer to the last generated question.
    
    Returns:
        str: 'yes' if the number is prime, 'no' otherwise
    """
    return {True: 'yes', False: 'no'}[is_prime(ANSWER)]
