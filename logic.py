

def calculate_total(student):
    return sum(student['marks'])

def calculate_average(student):
    return sum(student['marks']) / len(student['marks'])

def assign_grade(average):
    if average >= 90:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 60:
        return 'C'
    elif average >= 40:
        return 'D'
    else:
        return 'F'























def process_student(student):
    total = calculate_total(student)
    average = calculate_average(student)
    grade = assign_grade(average)
    student.update({"total": total, "average": average, "grade": grade})
    return student

def rank_students(students):
    return sorted(students, key=lambda x: x['total'], reverse=True)
