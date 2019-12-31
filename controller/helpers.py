import sys
from models.models import *


def check_exit(value):
    if value == 'exit':
        print('Quiting the program...\n')
        print('Bye!\n')
        return sys.exit()


def check_existing_subject(model, subject):
    """
    Checks if the subject exists
    """
    subjects = [
        exercise for exercise in model.exercises if exercise.subject == subject
        ]
    if len(subjects) > 0:
        return subjects[0]
    else:
        print(
            'You do not have this subject Create all the subjects before you continue')  # noqa
        subject = input(
                    'Try again, enter subject name:  \n')
        return check_existing_subject(model, subject)


def check_existing_student(model, name):
    """
    Checks if the student exists in the teacher class.
    """
    names = [student.name.lower() for student in model.students]
    if str(name).lower() in names:
        return name
    else:
        print('You do not have such student. Add all your students from the begining')  # noqa
        student = input('Try again. enter student name:  \n')
        return check_existing_student(model, student)


def get_student(model, name):
    """
    Gets existing student in the syste.
    """
    student = [student for student in model.students if student.name == name]
    if len(student) > 0:
        return student[0]
    else:
        print('You are not registered to take a test. Contact your teacher')  # noqa
        name = input('Try again. Type your name to start:  \n')
        return get_student_test(model, name)


def authenticate_user(model, password):
    """
    Ensures that only registered users can use the system.
    """
    for user in model.instances:
        if user.password != password:
            print('Wrong password')
            password = input('Enter the correct password to continue: \n')
            return authenticate_user(model, password)
        else:
            return model


def get_teacher(name):
    """
    Gets registered teacher in the system
    """
    if len(Teacher.instances) == 0:
        print('No teachers for this level with such a name')
    teachers = [
        teacher for teacher in Teacher.instances if teacher.name == name
        ]
    if len(teachers) == 0:
        print('No teacher with such name ({}) exist'.format(name))
        name = input('Enter the correct name: \n')
        return get_teacher(name)
    else:
        return teachers[0]


def display_semester_results(teacher, semester):
    """
    Displays all the semester results for a given semester.
    """
    students = teacher.get_semester_result(semester)
    if len(students) > 0:
        for student in students:
            print('* Student Name: \n' + student.name)
            for exercise in student.exercises:
                print('Subject: ' + exercise.subject)
                print('Semester: {}'.format(semester))
                print('Total Score: {}'.format(exercise.total_score))
                print(
                    'Average Score: {}'.format(exercise.average_score))
                print(
                    'Average Grade: {}'.format(exercise.grade))
    else:
        print('No results for this semester')


def display_questions(exercise, subject):
    """
    Dispaly all student questions for a particular quize subject
    """
    questions = exercise.questions
    if len(questions) == 0:
        print('No exercises')
    print('\033[92m SUJECT: {}. \033[00m '.format(subject))
    print('\033[92m ANSWERS CANNOT BE CHANGED ONCE SUBMITTED.\033[00m ')
    print('\033[92m There are {} question(s)\033[00m \n'.format(len(questions)))
    count = 1
    last = len(questions) - 1
    first = 0
    total_score = 0
    while first <= last:
        print('Question {}:  {}'.format(count,  questions[first].value))
        print('Choices: {}\n'.format(str(questions[first].choices)))
        answer = input('Enter your answer from the choices above: \n')
        while answer not in questions[first].choices:
            print('Enter one of the choices above')
            answer = input('Enter your answer from the choices above: \n')
        questions[first].answer_me(answer)
        total_score += questions[first].score
        count += 1
        first += 1
    exercise.total_score = total_score
