import random


def rule():
    print('What is the result of the expression?')


def generate_question():
    operators = ('+', '-', '*')
    first_num = random.randint(1, 50)  # NOSONAR
    second_num = random.randint(1, 50)  # NOSONAR
    operator = random.choice(operators)  # NOSONAR
    return f'{first_num} {operator} {second_num}'


def answer_to_question(question):
    first, operator, second = question.split()
    first_num, second_num = int(first), int(second)
    match operator:
        case '+':
            return str(first_num + second_num)
        case '-':
            return str(first_num - second_num)
        case '*':
            return str(first_num * second_num)
