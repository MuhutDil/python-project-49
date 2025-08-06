"""Arithmetic progression game module.
 
This module generates questions about missing elements
in arithmetic progressions for use in math quiz games.
It provides functionality to:
- Generate random arithmetic progressions
- Hide a random element in the progression
- Format the question and provide the correct answer
"""
import random

RULE = 'What number is missing in the progression?'


def question_and_answer():
    """Generates a question about a missing progression element and its answer.
 
    Returns:
        tuple[str, str]: A tuple containing:
            - question: The progression with one element replaced by '..'
            - answer: The correct missing element as a string
    """
    progression = generate_progression()
    hidden_index = random.randint(1, len(progression) - 1)  # NOSONAR
    hidden_element = progression[hidden_index]
    question = get_progression_string(progression, hidden_index)
    return question, str(hidden_element)


def generate_progression():
    """Generates an arithmetic progression sequence.

    Returns:
        list[int]: Generated arithmetic progression
    """
    start = random.randint(1, 100)  # NOSONAR
    step = random.randint(1, 10)  # NOSONAR
    len_progression = random.randint(5, 10)  # NOSONAR
    return [start + step * i for i in range(len_progression)]


def get_progression_string(progression, hide_index):
    """Formats a progression as a string with one hidden element.
 
    Args:
        progression (list[int]): Arithmetic progression to format
        hide_index (int): Index of element to hide (0-based)
 
    Returns:
        str: Space-separated string representation
        with hidden element marked as '..'
    """
    progression[hide_index] = '..'
    return ' '.join(map(str, progression))
