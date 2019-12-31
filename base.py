from models.models import *
from controller.validate import *


user = dict(name='admin', password='A1234', level=1, semester=1)
name = validate_user_string_value('teacher', user.get('name'))
password = validate_user_password(user.get('password'))
level = validate_user_int_value('level', user.get('level'))
semester = validate_semester_value('semester', user.get('semester'))
new_teacher = Teacher(name, password, level)
student = Student(name, password, new_teacher.level, semester, 1)
new_subject = Quiz('Math')
new_question = Question('What is 1 + 1', 2,  new_subject.subject)
new_choices = new_question.add_choices([1, 2, 3, 4])
new_subject.questions.append(new_question)
unlimited_choices = new_question.add_choices([1, 2, 3, 4, 3, 2, 4])
new_exercise = new_teacher.add_quiz(new_subject)
my_student = new_teacher.add_my_student(student)
assign_student_question = new_teacher.add_exercise_to_student(
    student.name, new_subject)
do_exercise = student.start_exercise(new_subject.subject)
answer = 2
do_question = student.exercises[0].questions[0].answer_me(answer)
grade_student = new_teacher.grade_student(student, new_subject)
