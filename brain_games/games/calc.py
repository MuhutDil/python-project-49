import random

ANSWER = None


def rule():
    print('What is the result of the expression?')


def generate_question():
    operators = ('+', '-', '*')
    first_num = random.randint(1, 50)  # NOSONAR
    second_num = random.randint(1, 50)  # NOSONAR
    operator = random.choice(operators)  # NOSONAR
    global ANSWER
    ANSWER = transform_math_expression(first_num, operator, second_num)
    return f'{first_num} {operator} {second_num}'


def transform_math_expression(first_num, operator, second_num):
    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def answer_to_question():
    return str(ANSWER)
