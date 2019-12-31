import sys


def check_exit(value):
    if value == 'exit':
        print('Quiting the program...\n')
        print('Bye!\n')
        return sys.exit()


def validate_student_data(name, level, id):
    if not isinstance(name, str):
        return False
    if len(name) <= 1:
        return False
    if not isinstance(level, int):
        return False
    return True


def display_questions(exercise, subject):
    questions = exercise.questions
    if len(questions) == 0:
        print('No exercises')
    print('\033[92m SUJECT: {}.'.format(subject))
    print('\033[92m ANSWERS CANNOT BE CHANGED ONCE SUBMITTED.')
    print('\033[92m There are {} question(s)\n'.format(len(questions)))
    count = 1
    last = len(questions) - 1
    first = 0
    total_score = 0
    while first <= last:
        print('Question {}:  {}'.format(count,  questions[first].value))
        print('Choices: {}\n'.format(str(questions[first].choices)))
        answer = input('Enter your answer from the choices above: \n')
        questions[first].answer_me(answer)
        print("Your answer", questions[first].answer)
        total_score += questions[first].score
        count += 1
        first += 1
    exercise.total_score = total_score
