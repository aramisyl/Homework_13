from typing import TypedDict
class StudentDTO(TypedDict):
    first_name: str
    last_name: str
    age: int
    course: int
    mean_grade: int

    def validate_name(self):
        if self.first_name[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            raise ValueError("First name should start from capital letter")
        if self.last_name[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            raise ValueError("Last name should start from capital letter")

    def validate_age(self):
        if self.age < 18 or self.age > 30:
            raise ValueError("Age should be between 18 and 30.")

    def validate_course(self):
        if self.course < 1 or self.course > 6:
            raise ValueError("Course should be between 1 and 6.")

    def validate_grade(self):
        if self.mean_grade < 1 or self.mean_grade > 100:
            raise ValueError("Grade should be between 1 and 100.")


student_dto = StudentDTO(**{'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'course': 3, 'mean_grade': 88})
print(student_dto)