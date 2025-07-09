import random

ANSWER = None


def rule():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')


def generate_question():
    num = random.randint(1, 100)  # NOSONAR
    global ANSWER
    ANSWER = num
    return num


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    upper_limit = int(num ** 0.5) + 1
    for i in range(3, upper_limit, 2):
        if num % i == 0:
            return False
    return True


def answer_to_question():
    return {True: 'yes', False: 'no'}[is_prime(ANSWER)]
