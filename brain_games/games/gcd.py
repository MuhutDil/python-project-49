"""Greatest Common Divisor (GCD) Game Module.
 
This module provides functionality for generating random
GCD questions and calculating their solutions. It's designed
for educational games or math practice tools where
users find the greatest common divisor of two numbers.
"""
import math
import random

RULE = 'Find the greatest common divisor of given numbers.'


def question_and_answer():
    """Generate a GCD question and its correct answer.
    
    Coordinates the question generation and answer calculation process.
    
    Returns:
        tuple: (question, answer) where:
            - question (str): Two numbers as
                space-separated string (e.g., "12 18")
            - answer (str): String representation of the GCD (e.g., "6")
    """
    question = generate_question()
    correct_answer = answer_to_question(question)
    return question, correct_answer


def generate_question():
    """Generate two random numbers for GCD calculation.
    
    Returns:
        str: Two space-separated integers between 1-100 (e.g., "24 36")
    """
    first_num = random.randint(1, 100)  # NOSONAR
    second_num = random.randint(1, 100)  # NOSONAR
    return f'{first_num} {second_num}'


def answer_to_question(question):
    """Calculate the GCD of two numbers from a question string.
    
    Args:
        question (str): Two space-separated integers (e.g., "12 18")
        
    Returns:
        str: GCD of the numbers as string
    """
    first_num, second_num = question.split()
    first_num, second_num = int(first_num), int(second_num)
    return str(math.gcd(first_num, second_num))
