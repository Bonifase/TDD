from controller.check_exit import validate_student_data


class Student:
    instances = []

    def __init__(self, name, password, semester, level, id):
        self.id = id
        self.name = name
        self.password = password
        self.semester = semester
        self.level = level
        self.exercises = []
        self.av_score = None
        self.instances.append(self)

    def start_exercise(self, subject):
        if len(self.exercises) == 0:
            return False
        for exercise in self.exercises:
            if exercise.subject == subject:
                return exercise


class Teacher:
    instances = []

    def __init__(self, name, password, level):
        self.name = name
        self.password = password
        self.level = level
        self.exercises = []
        self.students = []
        self.instances.append(self)

    def add_quize(self, quize):
        if quize:
            for exercise in self.exercises:
                if exercise.subject == quize.subject:
                    return False
            self.exercises.append(quize)

    def add_my_student(self, student):
        self.students.append(student)
        return self.students

    def add_exercise_to_student(self, name, subject):
        students = [student for student in self.students if name == student.name]  # noqa
        if len(students) > 0:
            student = students[0]
            for exercise in self.exercises:
                if subject.subject == exercise.subject:
                    student.exercises.append(subject)
                    return student.exercises
        else:
            return False

    def assign_grade(self, exercise, av_score):
        if av_score < 0.4:
            exercise.grade = 'E'
        elif av_score > 0.4 or av_score < 0.5:
            exercise.grade = 'D'
        elif av_score > 0.5 or av_score < 0.6:
            exercise.grade = 'C'
        elif av_score > 0.6 or av_score < 0.79:
            exercise.grade = 'B'
        else:
            exercise.grade = 'A'

    def grade_student(self, student, subject):
        if student in self.students:
            for exercise in student.exercises:
                if exercise.subject == subject.subject:
                    total_score = 0
                    count = 0
                    for question in exercise.questions:
                        if question.submitted is True:
                            count += 1
                            if question.score == 1:
                                total_score += 1
                            elif question.score == 0:
                                total_score += 0
                    av_score = total_score/count
                    self.assign_grade(exercise, av_score)
                    exercise.total_score = total_score
                    exercise.average_score = av_score
                    return exercise.total_score
        else:
            print('No students with such a name')
    
    def get_semester_result(self, semester):
        students = [student for student in self.students if student.semester == semester]  # noqa
        return students


class Question:
    def __init__(self, value, answer, subject):
        self.value = value
        self.choices = []
        self.subject = subject
        self.answer = answer
        self.submitted = False
        self.score = 0

    def add_choices(self, choices):
        if len(choices) > 4:
            return False
        for choice in choices:
            self.choices.append(choice)
        return True

    def answer_me(self, answer):
        if answer in self.choices and answer == self.answer:
            self.score = 1
            self.submitted = True
            return True
        else:
            self.answer = answer
            self.submitted = True


class Subject:

    def __init__(self, subject):
        self.subject = subject
        self.questions = []
        self.total_score = None
        self.average_score = None
        self.grade = None

    def add_question(self, question):
        subject = question.subject.subject
        if subject == self.subject:
            self.questions.append(question)
            return True
        return False
