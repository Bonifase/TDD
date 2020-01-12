import time
from models.models import *
from controller.helpers import *
from controller.validate import *

print('\n')
welcome = ['Welcome ', 'to ', 'classroom ', 'management','system. ', 'Follow ', 'the ', 'instructions ', 'to ', 'proceed.\n']
for item in welcome:
   print(item.upper(), end=" ", flush=True)
   time.sleep(0.4)
inst = ['NOTE:', 'To', 'exit', 'the', 'program', 'type', 'exit\n']
for item in inst:
   print(item.upper(), end=" ", flush=True)
   time.sleep(0.4)
print()
name = input(
    ('To setup your classroom, type in your name:  \n').upper())
check_exit(name)
name = validate_user_string_value('Enter name of teacher: \n', name)
password = input('Enter Password: \n')
check_exit(password)
password = validate_user_password(password)
level = input(
    '\033[92m Nice {}! Enter class level:\033[00m  \n'.format(name))
check_exit(level)
level = validate_user_int_value('level', level)
level = validate_semester_value('level', level)
teacher = Teacher(name, password, level)
enter = input(
    '\033[92m Hello {}, press ENTER to add students \033[00m \n'.format(teacher.name))
check_exit(enter)
password = input('Enter your password: \n')
teacher = authenticate_user(teacher, password)
number_of_students = input('How many students do you want to add?: \n')
check_exit(number_of_students)
number_of_students = validate_user_int_value(
    'number of students', number_of_students)
number_of_students = validate_total_items('students', number_of_students)
count = 0
while number_of_students > 0:
    semester = input('Enter semester: \n')
    check_exit(semester)
    semester = validate_user_int_value('semester', semester)
    semester = validate_semester_value('semester', semester)
    name = input('Enter Student name: \n')
    name = validate_user_string_value('name of student', name)
    check_exit(name)
    name = check_duplicate_user(teacher, name)
    check_exit(name)
    password = input('Enter student password: \n')
    password = validate_user_password(password)
    count += 1
    student = Student(name, password, semester, teacher.level, count)
    teacher.add_my_student(student)
    number_of_students -= 1
enter = input(
    "\033[92m You added {} students, press ENTER to add quizzes\n\033[00m".format(count))
check_exit(enter)

number_of_quizzes = input("How many quizzes do you want to add?: \n")
number_of_quizzes = validate_user_int_value(
    'number of subjects', number_of_quizzes)
check_exit(number_of_quizzes)
quizzes = validate_total_items('quizzes', number_of_quizzes)
count = 0
while quizzes > 0:
    name = input('Enter the quize subject: \n')
    validated_name = validate_user_string_value('quize subject', name)
    check_exit(validated_name)
    allowed_subject = check_subject('quize subject', validated_name)
    count += 1
    new_quiz = Quiz(allowed_subject)
    teacher.add_quiz(new_quiz)
    quizzes -= 1
enter = input(
    "\033[92m You have added {} subjects, press ENTER to add questions \033[00m \n".format(count))
check_exit(enter)

number_of_questions = input(
    "How many questions do you want to add?: \n")
check_exit(number_of_questions)
number_of_questions = validate_user_int_value(
    'number of questions', number_of_questions)
check_exit(number_of_questions)
questions = validate_total_items('questions', number_of_questions)
count = 0
while questions > 0:
    user_input = input('Enter quize subject: \n')
    subject = check_existing_subject(teacher,  user_input)
    check_exit(user_input)
    question = input('Enter the question: \n')
    check_exit(question)
    question = validate_question('question', question)
    answer = input('Enter answer: \n')
    answer = validate_question('answer', answer)
    check_exit(answer)
    question = Question(question, answer, subject)
    t = input("Enter the total number of choices: \n")
    check_exit(t)
    t = validate_user_int_value('number of choices', t)
    choice_number = validate_total_items('choices', t)
    choices = []
    while choice_number > 0:
        choice = input('Enter choice: \n')
        choice = validate_question('choice', choice)
        check_exit(choice)
        choices.append(choice)
        choice_number -= 1
    question.add_choices(choices)
    subject.add_question(question)
    teacher.add_quiz(subject)
    enter = input(
        "\033[92m  Question added!, press ENTER to continue \033[00m \n")
    count += 1
    questions -= 1
input(
    "\033[92m You added {} subjects for students,press ENTER to assign questions to your students \033[00m\n".format(count))  # noqa

T = input("How many students do you want to assign?: \n")
check_exit(T)
T = validate_user_int_value('number of students', T)
while T > len(teacher.students):
    print('You cannot assing more students that you have')
    T = input("How many students do you want to assign?: \n")
    T = validate_user_int_value('number of students', T)
check_exit(T)
count = 0
while T > 0:
    input_name = input('Enter the student name: \n')
    name = check_existing_student(teacher, input_name)
    check_exit(input_name)
    quizzes = input('How many quizzes for this student? \n')
    check_exit(quizzes)
    quizzes = validate_user_int_value('number of quizzes', quizzes)
    quizzes = validate_number_of_quizzes(teacher, quizzes)
    while quizzes > 0:
        subject = input('Enter the quiz subject name: \n')
        subject = check_existing_subject(teacher, subject)
        check_exit(subject)
        teacher.add_exercise_to_student(name, subject)
        quizzes -= 1
    T -= 1
input(
    "\033[92m You added exercises to students,press ENTER to allow them take the tests \033[00m\n")  # noqa

print('\033[92m Switching to student portal... \033[00m\n')
name = input('Welcome, type in your name to take the tests:  \n')
name = validate_user_string_value('your name', name)
check_exit(name)
student = get_student(teacher, name)
password = input('Enter your password: \n')
student = authenticate_user(student, password)
excercises = student.exercises
number_of_test = input('How many quizzes do you wish to take? \n')
check_exit(number_of_test)
number_of_test = validate_user_int_value('number of tests', number_of_test)
while number_of_test > len(student.exercises):
    print('You can only do upto {} quizzes'.format(len(student.exercises)))
    number_of_test = input('How many quizzes do you wish to take? \n')
    check_exit(number_of_test)
    number_of_test = validate_user_int_value('number of tests', number_of_test)

for excercise in excercises:
    while number_of_test > 0:
        subject = input('Welcome, type in your the subject:  \n')
        subject = validate_user_string_value('subject', subject)
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
name = validate_user_string_value('name of teacher \n', name)
password = input('Type in teacher password \n')
teacher = get_teacher(name)
teacher = authenticate_user(teacher, password)
student_name = input('Welcome {} enter student name: \n'.format(name))
student_name = validate_user_string_value('student name', student_name)
student = check_existing_student(teacher, student_name)
semester = input('Enter the semester: \n')
semester = validate_user_int_value('semster', semester)
semester = validate_semester_value('semester', semester)
subject = input('Enter the subject: \n')
subject = validate_user_string_value('subject', subject)
check_exit(subject)
subject = check_existing_subject(teacher, subject)
student = get_student(teacher, student)
teacher.grade_student(student, subject)
display_semester_results(teacher, semester)
