def display_student(student):
    print(f"ID: {student['id']} | Name: {student['name']}")
    print(f"Marks: {student['marks']}")
    print(f"Total: {student['total']} | Average: {student['average']:.2f} | Grade: {student['grade']}")
    print("-" * 50)

def display_all_students(students):
    print("\n===== Student Result Report =====")
    for student in students:
        display_student(student)
