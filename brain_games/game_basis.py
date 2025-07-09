import prompt

LIMIT_ANSWERS = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def ask_question(question):
    print(f'Question: {question}')
    return prompt.string('Your answer: ')


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
        user_answer = ask_question(question)
        correct_answer = answer_to_question()
        if correct_answer == user_answer:
            count_right_answer += 1
        else:
            status_game = False
            right_answer_data['user_answer'] = user_answer
            right_answer_data['correct_answer'] = correct_answer
            break
    endind_game(name, status_game, answer_data=right_answer_data) 
