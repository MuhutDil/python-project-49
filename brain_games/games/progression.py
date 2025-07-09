"""Arithmetic Progression Quiz Module.
 
This module generates arithmetic progressions with hidden elements
and tests the user's ability to identify the missing number.
It handles the full quiz cycle from question
generation to answer verification.
 
Global Variables:
    ANSWER (int|None):
        Stores the hidden number from the last generated progression.
 
Functions:
    rule(): Displays game instructions.
    generate_progression(): Creates a random arithmetic progression.
    generate_question(): Prepares a quiz question with hidden element.
    answer_to_question(): Reveals the correct answer.
"""
import random

ANSWER = None


def rule():
    """Prints the game instructions.
    
    Explains what the user should determine about the progression.
    """
    print('What number is missing in the progression?')


def generate_progression():
    """Generates a random arithmetic progression.
    
    Creates a sequence of numbers with
    constant difference to the preceding term.
    
    Returns:
        list: The generated progression as a list of integers
    """
    progression = []
    start = random.randint(1, 100)  # NOSONAR
    step = random.randint(1, 10)  # NOSONAR
    len_progression = random.randint(5, 10)  # NOSONAR
    for i in range(len_progression):
        progression.append(start + step * i)
    return progression


def generate_question():
    """Creates a quiz question with hidden element.
    
    1. Generates a progression
    2. Selects random element to hide
    3. Stores the hidden value in ANSWER
    4. Formats the progression with placeholder
    
    Returns:
        str: The progression with one element replaced by '..'
    """
    progression = generate_progression()
    hiden_index = random.randint(1, len(progression) - 1)  # NOSONAR
    global ANSWER
    ANSWER = progression[hiden_index]
    progression[hiden_index] = '..'
    return ' '.join(map(str, progression))


def answer_to_question():
    """Provides the correct hidden number.
    
    Returns:
        str: String representation of the hidden number
    """
    return str(ANSWER)
