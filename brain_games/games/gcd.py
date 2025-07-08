import math
import random


def rule():
    print('Find the greatest common divisor of given numbers.')


def generate_question():
    first_num = random.randint(1, 100)  # NOSONAR
    second_num = random.randint(1, 100)  # NOSONAR
    return f'{first_num} {second_num}'


def transform_math_expression(string_expression):
    first, second = string_expression.split()
    return int(first), int(second)


def answer_to_question(question):
    return str(math.gcd(*transform_math_expression(question)))
