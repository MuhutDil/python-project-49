"""Prime Number Identification Game Module.
 
This module provides functionality for a game that tests players' ability to
identify prime numbers between 1 and 100. It generates random numbers and
determines whether they are prime, returning the correct 'yes' or 'no' answer.
"""
import random

RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_game_conditions():
    """Generate a prime number identification question and its correct answer.
    
    Returns:
        tuple: (question, answer) where:
            - question (int): A randomly generated number between 1-100
            - answer (str): 'yes' if prime, 'no' if not prime
    """
    question = random.randint(1, 100)  # NOSONAR
    correct_answer = convert_to_answer(question)
    return question, correct_answer


def is_prime(num):
    """Check if a number is prime.
    
    Args:
        num (int): Number to check
        
    Returns:
        bool: True if prime, False otherwise
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


def convert_to_answer(question):
    """Convert prime check result to game answer format.
    
    Args:
        question (int): The number to evaluate
        
    Returns:
        str: 'yes' if prime, 'no' if not prime
    """
    return {True: 'yes', False: 'no'}[is_prime(question)]
