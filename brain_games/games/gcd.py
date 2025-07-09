import math
import random

ANSWER = None


def rule():
    print('Find the greatest common divisor of given numbers.')


def generate_question():
    first_num = random.randint(1, 100)  # NOSONAR
    second_num = random.randint(1, 100)  # NOSONAR
    global ANSWER
    ANSWER = math.gcd(first_num, second_num)
    return f'{first_num} {second_num}'


def answer_to_question():
    return str(ANSWER)
