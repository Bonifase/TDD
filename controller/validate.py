import re
from models.models import *

print(Teacher.instances)


def validate_user_password(password):
    if len(password) < 5 and len(password) < 10:
        print("Make sure your password is at least 5 letters and less than 10 letters")  # noqa
        password = input('Enter password again: ')
        return validate_user_password(password)
    elif re.search('[0-9]', password) is None:
        print("Make sure your password has a number in it")
        password = input('Enter password again: ')
        return validate_user_password(password)
    elif re.search('[A-Z]', password) is None: 
        print("Make sure your password has a capital letter in it")
        password = input('Enter password again: ')
        return validate_user_password(password)
    else:
        return password


def validata_user_string_value(identifier, value):
    if value.isdigit():
        print('\033[31m Type not allowed.')
        value = input(
                '\033[94m Type in {} again:  \n'.format(identifier))
        return validata_user_string_value(identifier, value)
    elif len(value) < 3:
        print('\033[31m Too short, Enter at least three characters.')
        value = input(
                    '\033[94m Type in {} again:  \n'.format(identifier))
        return validata_user_string_value(identifier, value)

    elif not isinstance(value, str):
        print('\033[31m Only string values are allowed.')
        value = input(
                '\033[94m Type in {} again:  \n'.format(identifier))
        return validata_user_string_value(identifier, value)
    else:
        return value


def validata_user_int_value(identity, value):
    value = str(value)
    if len(value) > 0:
        if not value.isdigit():
            print('\033[31m Only integer values are allowed.')
            value = input(
                    '\033[94m Type in {} again:  \n'.format(identity))
            return validata_user_int_value(identity, value)
        return int(value)
    else:
        print('\033[31m Too short, Enter a value.')
        value = input(
                    '\033[94m Type in {} again:  \n'.format(identity))
        return validata_user_int_value(identity, value)


def validate_semester_value(value):
    allowed_semesters = [1, 2, 3]
    print(value)
    if value in allowed_semesters:
        return value
    else:
        print('Enter integer value between 1-3.')
        value = input('Enter a valid semester value')
        return validate_semester_value(value)


def check_subject(identity, subject):
    allowed_subjects = ['python', 'data structures', 'algorithm', 'oop']
    if subject not in allowed_subjects:
        print('\033[31m That subject ({}) is not offered here. Contact school administrator'.format(subject))  # noqa
        value = input(
                    '\033[94m Type in {} again:  \n'.format(identity))
        return check_subject(identity, value)
    return subject


def check_existing_subject(model, subject):
    subjects = [
        exercise for exercise in model.exercises if exercise.subject == subject
        ]
    if len(subjects) > 0:
        return subjects[0]
    else:
        print(
            '\033[31m You do not have this subject Create all the subjects before you continue')  # noqa
        subject = input(
                    '\033[94m Try again, enter subject name:  \n')
        return check_existing_subject(model, subject)


def check_existing_student(model, name):
    names = [student.name.lower() for student in model.students]
    if str(name).lower() in names:
        return name
    else:
        print('\033[31m You do not have such student. Add all your students from the begining')  # noqa
        student = input(
                    '\033[01m Try again. enter student name:  \n')
        return check_existing_student(model, student)


def get_student(model, name):
    student = [student for student in model.students if student.name == name]
    if len(student) > 0:
        return student[0]
    else:
        print('\033[31m You are not registered to take a test. Contact your teacher')  # noqa
        name = input(
                    '\033[01m Try again. Type your name to start:  \n')
        return get_student_test(model, name)


def authenticate_user(model, password):
    for user in model.instances:
        if user.password != password:
            print('Wrong password')
            password = input('Enter the correct password to continue: \n')
            return authenticate_user(model, password)
        else:
            return model


def get_teacher(name):
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
    students = teacher.get_semester_result(semester)
    if len(students) > 0:
        for student in students:
            print('* Student Name: ' + student.name)
            for exercise in student.exercises:
                print('Subject: ' + exercise.subject)
                print('Semester: {}'.format(semester))
                print('Total Score: {}'.format(exercise.total_score))
                print('Average Score: {}'.format(exercise.average_score)
                )
                print('Average Grade: {}'.format(exercise.grade)
                )
    else:
        print('No results for this semester')
