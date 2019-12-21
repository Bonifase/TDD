import unittest
from base import *


class TestCase(unittest.TestCase):
    def test_add_teacher(self):
        response = new_teacher
        self.assertEqual(response.name, 'teacher')

    def test_add_student(self):
        teacher = new_teacher
        response = new_student
        self.assertEqual(response.name, 'james')

    def test_cannot_add_invalid_student_name(self):
        teacher = new_teacher
        response = Student('james', 'level', 1)
        self.assertEqual(hasattr(response, 'james'), False)

    def test_cannot_add_invalid_level(self):
        teacher = new_teacher
        response = Student('james', teacher.level, "jnjnm")
        self.assertEqual(hasattr(response, 'james'), False)

    def test_add_quize(self):
        response = new_subject
        self.assertEqual(response.subject, 'Math')

    def test_cannot_add_duplicate_quize(self):
        subject = new_subject
        response = new_subject
        self.assertEqual(hasattr(response, 'Math'), False)

    def test_add_question(self):
        subject = new_subject
        question = new_question
        self.assertEqual(question.subject, subject.subject)
        choices = new_choices
        self.assertEqual(question.choices[0], 1)

    def test_add_limited_question_choices(self):
        subject = new_subject
        question = new_question
        choices = unlimited_choices
        self.assertEqual(choices, False)

    def test_add_limited_question_choices(self):
        subject = new_subject
        question = new_question
        choices = unlimited_choices
        self.assertEqual(choices, False)

    def test_assign_student_to_teacher(self):
        response = my_student
        self.assertEqual(len(response), 1)

    def test_asign_question_to_student(self):
        """
        Test teacher can asign question to students works
        """
        asign_exercise = assign_student_question
        self.assertEqual(len(asign_exercise), 1)

    def test_student_do_assignment(self):
        """
        Test student can do exercise works
        """
        tackle_question = do_exercise
        self.assertEqual(tackle_question, 2)

    def test_submit_exercise(self):
        """
        Test student can submit exercise
        """
        tackle_question = do_exercise
        self.assertEqual(tackle_question, 2)

    def test_grade_student(self):
        """
        Test teacher can grade student
        """
        average_score = grade_student
        self.assertEqual(average_score, 1.0)


if __name__ == '__main__':
    unittest.main()
