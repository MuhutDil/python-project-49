"""Arithmetic Expression Game Module.
 
This module provides functionality for generating simple math expression
questions and calculating their correct answers. It supports three basic
operations:
addition (+),
subtraction (-),
multiplication (*).
 
The main interface is generate_game_conditions() which returns
a tuple containing:
- A string math expression (e.g., "3 + 5")
- The correct answer as a string (e.g., "8")
"""
import random

RULE = 'What is the result of the expression?'


def generate_game_conditions():
    """Generate a random arithmetic question and its correct answer.
    
    Coordinates the question generation and answer calculation process.
    
    Returns:
        tuple: (question, answer) where:
            - question (str): Formatted math expression (e.g., "4 * 7")
            - answer (str): String representation of the correct result
    """
    question = generate_question()
    correct_answer = calculate_math_expression(question)
    return question, str(correct_answer)


def calculate_math_expression(expression):
    """Evaluate a mathematical expression string.
    
    Args:
        expression (str): Math expression in format "num op num" (e.g., "5 + 3")
        
    Returns:
        int: Calculated result of the expression
    """
    first_num, operator, second_num = expression.split()
    first_num, second_num = int(first_num), int(second_num)
    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def generate_question():
    """Generate a random arithmetic expression.
    
    Randomly selects:
    - Two integers between 1 and 50 (inclusive)
    - One operator from '+', '-', '*'
    
    Returns:
        str: Formatted expression string (e.g., "15 * 3")
    """
    operators = ('+', '-', '*')
    first_num = random.randint(1, 50)  # NOSONAR
    second_num = random.randint(1, 50)  # NOSONAR
    operator = random.choice(operators)  # NOSONAR
    return f'{first_num} {operator} {second_num}'
