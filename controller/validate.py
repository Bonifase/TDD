import re
# from models.models import *
# from controller.helpers import check_exit


def validate_user_password(password):
    """
    Validates user passwords.
    Ensures that user enter a strong password.
    """
    if len(password) < 5 and len(password) < 10:
        raise ValueError("Make sure your password is at least 5 letters and less than 10 letters")  # noqa
    elif re.search('[0-9]', password) is None:
        raise ValueError("Make sure your password has a number in it")
    elif re.search('[A-Z]', password) is None:
        raise ValueError("Make sure your password has a capital letter in it")

    return True
# client code :
# user_input = ''
# ADD THIS PURELY FOR THE CLI
def get_user_input(input_message, validator_fn):
    try:
        user_input = input(input_message)
        validator_fn(user_input)
    except ValueError as e:
        print(e)
        user_input = get_user_input(input_message, validator_fn)

    return user_input  # this is a valid user input 


def validate_user_string_value(value):
    """
    Validates string values.
    Ensures that user enter a string value where string
    inputs are required.
    Returns a string value
    """
    name_length = 3
    if len(value) < name_length:
        raise ValueError('User name must contain more than three characters')
    elif not isinstance(value, str):
        raise ValueError('Only string values are allowed.')
    elif not value.isalnum():
        raise ValueError('Must be a string')
    elif value.isdigit():
        raise ValueError('Must be a string')

    return True


def validate_user_level_value(value):
    """
    Validates integer values.
    Ensures that user enter an interger value where integer
    inputs are required.
    Returns an integer value
    """
    value = str(value)
    allowed_levels = [1, 2, 3]
    if len(value) > 0:
        if not value.isdigit():
            raise ValueError('Only integer values are allowed.')
        if int(value) not in allowed_levels:
            raise ValueError('Level not allowed')
        return True
    else:
        raise ValueError('Too short, Enter a value.')
        
def validate_total_items(identity, value):
    """
    Limits the number of items to be created.
    this includes number of students, quizzes, questions and choices.
    Returns an integer value
    """
    if identity == 'students':
        if value > 40 or value <= 0:
            print('You can only add a minimum of 1 and a maximum of 40 students.')
            value = input('Type in number of students again:  \n')
            value = validate_user_int_value(identity, value)
            return validate_total_items(identity, value)
        return value
    elif identity == 'quizzes':
        if value > 8 or value <= 0:
            print('You can only add a minimum of 1 and a maximum of 8 quizes.')
            value = input('Type in number of quizzes again:  \n')
            value = validate_user_int_value(identity, value)
            return validate_total_items(identity, value)
        else:
            return value
    elif identity == 'questions':
        if value > 30 or value <= 0:
            print(
                'You can only add a minimum of 1 and a maximum of 30 questions.')
            value = input('Type in number of questions again:  \n')
            value = validate_user_int_value(identity, value)
            return validate_total_items(identity, value)
        else:
            return value
    elif identity == 'choices':
        if value > 6:
            print('You can only add a minimum of 1 and a maximum of 6 choices.')
            value = input('Type in number of choices again:  \n')
            value = validate_user_int_value(identity, value)
            return validate_total_items(identity, value)
        else:
            return value


def validate_semester_value(value):
    """
    validates semester
    Ensures that user enter only allowed semester values
    Set allowed semester values as 1, 2, 3
    """
    allowed_semesters = [1, 2, 3]
    if value in allowed_semesters:
        return True
    else:
        raise ValueError('Enter integer value between 1-3.')
        value = input('Enter a valid semester value: \n')
        value = validate_user_int_value(identity, value)
        return validate_semester_value(identity, value)
        

class ValidateQuestion:

    def validate_question(value):
        """
        validates question
        Ensures that user enter a meaningful question
        """
        question_length = 4
        if len(value) < 4 or value.isspace():
            print('Please enter some value.')
            value = input('Enter a valid question value: \n')
            return validate_question(identity, value)
        else:
            return value

    def validate_answer(value):
        if len(value) == 0 or value.isspace():
            print('Please enter some value.')
            value = input('Enter a valid answer value: \n')
            return validate_question(identity, value)
        else:
            return value
            
    def validate_choice(value):
        if len(value) == 0 or value.isspace():
            print('Please enter some value.')
            value = input('Enter a valid choice value: \n')
            return validate_question(identity, value)
        else:
            return value


def validate_number_of_quizzes(model, quizzes):
    """
    check if the number of quizzes exist
    """
    if quizzes == 0 or quizzes > len(model.exercises):
        print('You can asign a minimum of 1 or a maximum of {}'.format(len(model.exercises)))
        quizzes = input('How many quizzes for this student? \n')
        check_exit(quizzes)
        quizzes = validate_user_int_value('number of quizzes', quizzes)
        return validate_number_of_quizzes(model, quizzes)
    else:
        return quizzes


def check_subject(identity, subject):
    allowed_subjects = ['python', 'data structures', 'algorithm', 'oop', 'JavaScript', ]
    if subject not in allowed_subjects:
        print('That subject ({}) is not offered here. Contact school administrator\n'.format(subject))  # noqa
        print('Allowed subjects are: python, data structures, algorithm, oop, Python, JavaScript')
        value = input('Type in {} again:  \n'.format(identity))
        return check_subject(identity, value)
    return subject


def check_duplicate_user(teacher, name):
    """
    Ensures that no duplicate entry is added
    """
    if len(teacher.students) > 0:
        for student in teacher.students:
            if student.name == name:
                print('Student already exist, type a different name')
                name = input('Enter name again: \n')
                name = validate_user_string_value('name of user', name)
                return check_duplicate_user(teacher, name)
            else:
                return name
    else:
        return name
