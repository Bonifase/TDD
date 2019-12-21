import sys
from objects import *
from check_exit import check_exit
from validate import validata_user_int_value, validata_user_string_value

print('Type exit to Quit\n')
name = str(input(
    '\033[94m To setup your classroom, type in your name:  \n'))
check_exit(name)
while not validata_user_string_value(name):
    print('\033[31m Type not allowed.')
    name = str(input(
    '\033[94m To setup your classroom, type in your name:  \n'))
level = input(
    '\033[92m Nice {}! Enter class level:\033[00m  \n'.format(name))
check_exit(level)
while not validata_user_int_value(level):
    print('\033[31m Type not allowed.')
    level = input(
    '\033[92m Enter class level {}:\033[00m  \n'.format(name))
    check_exit(level)
teacher = Teacher(name, level)
enter = input(
    "\033[92m Hello {}, press ENTER to add students \033[00m \n".format(teacher.name))
check_exit(enter)

T = input("\033[94m Enter the total number of students: \n")
check_exit(T)
if not validata_user_int_value(T):
    print('\033[31m Tye not allowed, ENTER a number')
    T = input("\033[94m Enter the total number of students: \n")
count = 0
T = int(T)
while T > 0:
    name = str(input('Enter Student name: \n'))
    check_exit(name)
    count += 1
    student = Student(name, teacher.level, count)
    teacher.add_my_student(student)
    T -= 1
enter = input(
    "\033[92m You added {} students, press ENTER to add exercises\n\033[00m".format(count))
check_exit(enter)
T = input("Enter the total number of subjects: \n")
while not validata_user_int_value(T):
    print('\033[31m Type not allowed.')
    T = input(
    '\033[92m Enter the total number of subjects: \n')
    check_exit(T)
check_exit(T)
T = int(T)
count = 0
while T > 0:
    name = str(input('Enter Subject name: \n'))
    check_exit(name)
    count += 1
    quize = Quize()
    subject = quize.add_subject(name)
    T -= 1
enter = input(
    "\033[92m You added {} subjects, press ENTER to add questions \033[00m \n".format(count))
check_exit(enter)

T = input("Enter the total number of questions: \n")
while not validata_user_int_value(T):
    print('\033[31m Type not allowed.')
    T = input(
    '\033[92m Enter the total number of questions: \n')
    check_exit(T)
check_exit(T)
count = 0
while T > 0:
    question = str(input('Enter question: \n'))
    check_exit(question)
    subject = str(input('Enter subject: \n'))
    check_exit(subject)
    quest = Question(question, subject)
    t = int(input("Enter the total number of choices: \n"))
    check_exit(t)
    choices = []
    while t > 0:
        choice = str(input('Enter choice: \n'))
        check_exit(choice)
        choices.append(choice)
        t -= 1
    enter = input("\033[92m  Question added!, press ENTER to add next questions \033[00m \n")
    quest.add_choices(enter)
    count += 1
    T -= 1
input(
    "\033[92m You added exercises for students,press ENTER to assign questions to your students \033[00m\n")  # noqa
T = int(input('Enter the number of students: \n'))
check_exit(str(T))
while int(T) > 0:
    name = input('Enter student name: \n')
    student = Student(name, teacher.level)
    teacher.add_my_student(student)
    T -= 1
