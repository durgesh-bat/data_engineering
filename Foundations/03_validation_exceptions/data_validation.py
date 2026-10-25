# print(len(student['name']))
def name_validator(name: str):
    if len(name.strip()) == 0:
        return False
    return True

def age_validator(age:str):
    try:
        return int(age)>=0
    except ValueError:
        return False
    
def marks_validator(marks:str):
    try:
        marks = int(marks)
    except ValueError:
        return False
    if marks<0 or  marks>100:
        return False
    return True

def validate_title(title):

    if title is None:
        return False, "Title is missing"

    if not isinstance(title, str):
        return False, "Title must be a string"

    title = title.strip()

    if len(title) == 0:
        return False, "Title is empty"

    if len(title) <= 2:
        return False, "Title is too short"

    return True, None


def validate_student(student):
    try:
        if not name_validator(student['name']):
            return False
        if not age_validator(student['age']):
            return False
        if not marks_validator(student['marks']):
            return False
        return True
    except Exception as e:
        print("Exception: ",e)
        return False
