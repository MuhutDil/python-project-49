import prompt

LIMIT_ANSWERS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def endind_game(name, status_game, *, answer_data):
    if status_game:
        print(f'Congratulations, {name}!')
    else:
        print(
            f"'{answer_data['user_answer']}' is wrong answer ;(."
            f"Correct answer was '{answer_data['correct_answer']}'.\n"
            f"Let's try again, {name}!"
        )


def game(rule, generate_question, answer_to_question):
    name = welcome_user()
    rule()
    count_right_answer = 0
    status_game = True
    right_answer_data = {}
    while count_right_answer < LIMIT_ANSWERS:
        question = generate_question()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = answer_to_question(question)
        right_answer = (correct_answer == user_answer)
        if right_answer:
            count_right_answer += 1
        else:
            status_game = False
            right_answer_data['user_answer'] = user_answer
            right_answer_data['correct_answer'] = correct_answer
            break
    endind_game(name, status_game, answer_data=right_answer_data) 
