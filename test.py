import unittest
from base import *


class TestCase(unittest.TestCase):
    def test_add_teacher(self):
        """
        Test the systen can register teachers
        """
        response = new_teacher
        self.assertEqual(response.name, 'admin')

    def test_add_student(self):
        """
        Test teachers add students
        """
        teacher = new_teacher
        response = student
        self.assertEqual(response.name, 'admin')

    def test_cannot_add_invalid_student_name(self):
        """
        Test teacher cannot add student with invalid name
        """
        teacher = new_teacher
        response = Student('james', 'password', 'semester', 'level', 1)
        self.assertEqual(hasattr(response, 'james'), False)

    def test_cannot_add_invalid_level(self):
        """
        Test the system cannot add stuent with level tha does not exist.
        """
        teacher = new_teacher
        response = Student('james', 'password', 1, teacher.level, "jnjnm")
        self.assertEqual(hasattr(response, 'james'), False)

    def test_add_quize(self):
        """
        Test teachers add quizzes
        """
        response = new_subject
        self.assertEqual(response.subject, 'Math')

    def test_cannot_add_duplicate_quize(self):
        """
        Test teachers cannot add duplicate quizzes
        """
        subject = new_subject
        response = new_subject
        self.assertEqual(hasattr(response, 'Math'), False)

    def test_add_question(self):
        """
        Test teachers add questions
        """
        subject = new_subject
        question = new_question
        self.assertEqual(question.subject, subject.subject)
        choices = new_choices
        self.assertEqual(question.choices[0], 1)

    def test_add_limited_question_choices(self):
        """
        Test teachers add multiple choices to questions
        """
        subject = new_subject
        question = new_question
        choices = unlimited_choices
        self.assertEqual(choices, False)

    def test_add_limited_question_choices(self):
        """
        Test teachers add multiple choices to questions
        """
        subject = new_subject
        question = new_question
        choices = unlimited_choices
        self.assertEqual(choices, False)

    def test_assign_student_to_teacher(self):
        """
        Test teachers add students to their classes
        """
        response = my_student
        self.assertEqual(len(response), 1)

    def test_asign_question_to_student(self):
        """
        Test teacher asign quiz to students.
        """
        asign_exercise = assign_student_question
        self.assertEqual(len(asign_exercise), 1)

    def test_student_do_quiz(self):
        """
        Test student can do quize.
        """
        tackle_question = do_exercise
        self.assertEqual(hasattr(tackle_question, 'score'), False)

    def test_grade_student(self):
        """
        Test teacher can grade student
        """
        average_score = grade_student
        self.assertEqual(average_score, 1.0)


if __name__ == '__main__':
    unittest.main()
