import random

ANSWER = None


def rule():
    print('What number is missing in the progression?')


def generate_progression():
    progression = []
    start = random.randint(1, 100)  # NOSONAR
    step = random.randint(1, 10)  # NOSONAR
    len_progression = random.randint(5, 10)  # NOSONAR
    for i in range(len_progression):
        progression.append(start + step * i)
    return progression


def generate_question():
    progression = generate_progression()
    hiden_index = random.randint(1, len(progression) - 1)  # NOSONAR
    global ANSWER
    ANSWER = progression[hiden_index]
    progression[hiden_index] = '..'
    return ' '.join(map(str, progression))


def answer_to_question(question):
    return str(ANSWER)
