import random


def rule():
    print('What is the result of the expression?')


def generate_question():  # NOSONAR
    operators = ('+', '-', '*')
    first_num = random.randint(1, 50)
    second_num = random.randint(1, 50)
    operator = random.choice(operators)
    return f'{first_num} {operator} {second_num}'


def transform_math_expression(string_expression):
    first, operator, second = string_expression.split()
    first_num, second_num = int(first), int(second)
    match operator:
        case '+':
            return first_num + second_num
        case '-':
            return first_num - second_num
        case '*':
            return first_num * second_num


def answer_to_question(question):
    return str(transform_math_expression(question))
