import sys
from models.models import *
from controller.check_exit import *
from controller.validate import *

print('\n')
print('NOTE: To exit the program type exit\n')
name = input(
    'To setup your classroom, type in your name:  \n')
check_exit(name)
name = validata_user_string_value('Enter name of teacher: \n', name)
password = input('Enter Password: \n')
check_exit(password)
password = validate_user_password(password)
level = input(
    '\033[92m Nice {}! Enter class level:\033[00m  \n'.format(name))
check_exit(level)
level = validata_user_int_value('level', level)
teacher = Teacher(name, password, level)
enter = input(
    '\033[92m Hello {}, press ENTER to add students \033[00m \n'.format(teacher.name))
check_exit(enter)
password = input('Enter your password: \n')
teacher = authenticate_user(teacher, password)
T = input('Enter the total number of students: \n')
check_exit(T)
T = validata_user_int_value('number of students', T)
count = 0
while T > 0:
    semester = input('Enter semester: \n')
    check_exit(semester)
    semester = validata_user_int_value('semester', semester)
    name = input('Enter Student name: \n')
    name = validata_user_string_value('name of student', name)
    check_exit(name)
    password = input('Enter student password: \n')
    password = validate_user_password(password)
    count += 1
    student = Student(name, password, semester, teacher.level, count)
    teacher.add_my_student(student)
    T -= 1
enter = input(
    "\033[92m You added {} students, press ENTER to add exercises\n\033[00m".format(count))
check_exit(enter)

T = input("Enter the total number of subjects: \n")
T = validata_user_int_value('number of subjects', T)
check_exit(T)
count = 0
while T > 0:
    name = input('Enter Subject name: \n')
    validated_name = validata_user_string_value('subject name', name)
    check_exit(validated_name)
    allowed_subject = check_subject('subject name', validated_name)
    count += 1
    new_subject = Subject(allowed_subject)
    teacher.add_quize(new_subject)
    T -= 1
enter = input(
    "\033[92m You have added {} subjects, press ENTER to add questions \033[00m \n".format(count))
check_exit(enter)

T = input("Enter the total number of questions: \n")
check_exit(T)
T = validata_user_int_value('number of questions', T)
check_exit(T)
count = 0
while T > 0:
    user_input = input('Enter subject: \n')
    subject = check_existing_subject(teacher,  user_input)
    check_exit(user_input)
    question = input('Enter question: \n')
    check_exit(question)
    answer = input('Enter answer: \n')
    check_exit(answer)
    question = Question(question, answer, subject)
    t = input("Enter the total number of choices: \n")
    check_exit(t)
    t = validata_user_int_value('number of choices', t)
    choices = []
    while t > 0:
        choice = input('Enter choice: \n')
        check_exit(choice)
        choices.append(choice)
        t -= 1
    question.add_choices(choices)
    subject.add_question(question)
    teacher.add_quize(subject)
    enter = input(
        "\033[92m  Question added!, press ENTER to continue \033[00m \n")
    count += 1
    T -= 1
input(
    "\033[92m You added {} subjects for students,press ENTER to assign questions to your students \033[00m\n".format(count))  # noqa

T = input("Enter how many students: \n")
check_exit(T)
T = validata_user_int_value('number of students', T)
check_exit(T)
count = 0
while T > 0:
    input_name = input('Enter the student name: \n')
    name = check_existing_student(teacher, input_name)
    check_exit(input_name)
    t = input('How many subjects for this student? ')
    check_exit(t)
    t = validata_user_int_value('number of subjects', t)
    while t > 0:
        subject = input('Enter the subject name: \n')
        subject = check_existing_subject(teacher, subject)
        check_exit(subject)
        teacher.add_exercise_to_student(name, subject)
        t -= 1
    T -= 1
input(
    "\033[92m You added exercises to students,press ENTER to allow them take the tests \033[00m\n")  # noqa

print('\033[92m Switching to student portal... \033[00m\n')
name = input('Welcome, type in your name to take the tests:  \n')
name = validata_user_string_value('your name', name)
check_exit(name)
student = get_student(teacher, name)
password = input('Enter your password: \n')
student = authenticate_user(student, password)
excercises = student.exercises
number_of_test = input('How many tests dou you wish to take? \n')
check_exit(number_of_test)
number_of_test = validata_user_int_value('number of tests', number_of_test)

for excercise in excercises:
    while number_of_test > 0:
        subject = input('Welcome, type in your the subject:  \n')
        subject = validata_user_string_value('subject', subject)
        while excercise.subject != subject:
            print('You are not enrollred for that  subject, contact your teacher\n')
            subject = input('Type in the subject you want to take:  \n') 
        display_questions(excercise, subject)
        print('You completed your exercise successfully. You scored {}\n'.format(excercise.total_score))
        number_of_test -= 1
finish = input('Press enter to finish the test\n')

input('Press enter to grade the your students \n')
name = input('Enter your name: \n')
check_exit(name)
name = validata_user_string_value('name of teacher \n', name)
password = input('Type in teacher password \n')
teacher = get_teacher(name)
teacher = authenticate_user(teacher, password)
student_name = input('Welcome {} enter student name: \n'.format(name))
student_name = validata_user_string_value('student name', student_name)
student = check_existing_student(teacher, student_name)
semester = input('Enter the semester: \n')
semester = validata_user_int_value('semster', semester)
semester = validate_semester_value(semester)
subject = input('Enter the subject: \n')
subject = validata_user_string_value('subject', subject)
check_exit(subject)
subject = check_existing_subject(teacher, subject)
student = get_student(teacher, student)
print(teacher.grade_student(student, subject))
display_semester_results(teacher, semester)

