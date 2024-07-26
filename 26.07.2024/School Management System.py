class Student:
    def __init__(self, name, grade, subjects):
        self.name = name
        self.grade = grade
        self.subjects = subjects
def students_in_subject(students, subject):
    return [student.name for student in students if subject in student.subjects]
students = [Student("Alice", 10, ["Math", "Science"]), Student("Bob", 10, ["English", "Math"]), Student("Charlie", 11, ["Science"])]
print(students_in_subject(students, "Math"))  
