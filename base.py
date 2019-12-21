from objects import *

new_teacher = Teacher('teacher', 1)
new_student = Student('james', new_teacher.level, 1)
subject = Subject()
new_subject = subject.add_subject('Math')
new_question = Question('What is 1 + 1', 2,  new_subject.subject)
new_choices = new_question.add_choices([1, 2, 3, 4])
add_question = subject.add_question(new_question)
unlimited_choices = new_question.add_choices([1, 2, 3, 4, 3, 2, 4])
new_exercise = new_teacher.add_quize(subject)
my_student = new_teacher.add_my_student(new_student)
assign_student_question = new_teacher.add_exercise_to_student(
    new_student, subject)
do_exercise = new_student.do_exercise(subject.subject, 2)
submit_exercise = new_student.submitted
grade_student = new_teacher.grade_student(new_student, new_subject.subject)
