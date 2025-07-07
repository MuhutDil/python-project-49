import random


def rule():
    print('Answer "yes" if the number is even, otherwise answer "no".')


def generate_question():
    return random.randint(1, 100)  # NOSONAR


def is_even(num):
    return True if num % 2 == 0 else False


def answer_to_question(question):
    return {True: 'yes', False: 'no'}[is_even(question)]
