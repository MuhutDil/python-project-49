"""Greatest Common Divisor (GCD) Quiz Module.
 
This module generates pairs of random numbers and calculates their GCD.
It's designed for quiz systems where users need to find the GCD of two numbers.
 
The module provides:
- Random number pair generation (1-100)
- GCD calculation using Python's math.gcd()
- Consistent answer storage between question generation and verification
 
Global Variables:
    ANSWER (int|None): 
        Stores the GCD of the last generated pair. Initialized as None.
 
Functions:
    rule(): Prints the game instructions.
    generate_question(): 
        Generates a random number pair and calculates their GCD.
    answer_to_question(): Returns the correct GCD answer.
"""
import math
import random

ANSWER = None


def rule():
    """Prints the game instructions.
    
    Explains to the user what mathematical operation they should perform.
    """
    print('Find the greatest common divisor of given numbers.')


def generate_question():
    """Generates a random number pair and calculates their GCD.
    
    Generates two random integers between 1 and 100, 
    calculates their GCD using math.gcd(), stores the result
    in the global ANSWER, and returns the number pair as a string.
    
    Returns:
        str: The two generated numbers as
             a space-separated string (e.g., "36 48")
    """
    first_num = random.randint(1, 100)  # NOSONAR
    second_num = random.randint(1, 100)  # NOSONAR
    global ANSWER
    ANSWER = math.gcd(first_num, second_num)
    return f'{first_num} {second_num}'


def answer_to_question():
    """Provides the correct GCD answer for the last generated pair.
    
    Returns:
        str: String representation of the stored GCD answer
    """
    return str(ANSWER)
