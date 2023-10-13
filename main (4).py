class Student:
    def __init__(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
    return sorted_students

students = [
    Student("gayathri", "001", 3.8),
    Student("sangeetha", "002", 3.5),
    Student("gayathri", "003", 3.9),
    Student("aarithi", "004", 3.7),
]

sorted_students = sort_students(students)

for student in sorted_students:
    print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,student.roll_number,student.cgpa))
