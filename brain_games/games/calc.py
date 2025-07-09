"""Math Expression Generator Module.
 
This module generates simple arithmetic expression questions and
calculates their answers.
It's designed to be used in quiz/game systems where users need
to solve math problems.
 
The module provides:
- Question generation with random numbers and operators
- Answer calculation
- Consistent storage of the correct answer between 
  question generation and answer checking
 
Example usage:
    >>> rule()
    What is the result of the expression?
    >>> question = generate_question()
    >>> print(question)
    15 * 3
    >>> answer = answer_to_question()
    >>> print(answer)
    45
 
Global Variables:
    ANSWER (int|None): 
        Stores the correct answer to the last generated question.
        Initialized as None and updated when generating questions.
 
Functions:
    rule(): Displays the game instructions.
    generate_question(): Generates a random math expression question.
    transform_math_expression(first_num, operator, second_num):
        Calculates expression result.
    answer_to_question(): Returns the correct answer
        to the last generated question.
"""
import random

ANSWER = None


def rule():
    """Prints the game rule/instruction.
    
    The instruction explains what the user
    should do with the generated questions.
    """
    print('What is the result of the expression?')


def transform_math_expression(first_num, operator, second_num):
    """Calculates the result of a math expression.
    
    Args:
        first_num (int): The first operand
        operator (str): The arithmetic operator (+, -, *)
        second_num (int): The second operand
    
    Returns:
        int: The result of the arithmetic operation
    """
    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def generate_question():
    """Generates a random arithmetic expression question.
    
    Randomly selects:
    - Two integers between 1 and 50
    - One operator from +, -, *
    
    Stores the correct answer in the global ANSWER variable.
    
    Returns:
        str: The generated math expression as a string (e.g., "5 + 3")
    """
    operators = ('+', '-', '*')
    first_num = random.randint(1, 50)  # NOSONAR
    second_num = random.randint(1, 50)  # NOSONAR
    operator = random.choice(operators)  # NOSONAR
    global ANSWER
    ANSWER = transform_math_expression(first_num, operator, second_num)
    return f'{first_num} {operator} {second_num}'


def answer_to_question():
    """Provides the correct answer to the last generated question.
    
    Returns:
        str: The string representation of the stored answer
    """
    return str(ANSWER)
