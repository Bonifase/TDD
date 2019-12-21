def validate_student_data(name, level, id):
    if not isinstance(name, str):
        return False
    if len(name) <= 1:
        return False
    if not isinstance(level, int):
        return False
    return True


def validata_user_string_value(name):
    if name:
        if name.isdigit():
            return False
        else:
            return True


def validata_user_int_value(number):
    if number:
        if not number.isdigit():
            return False
        else:
            return True
